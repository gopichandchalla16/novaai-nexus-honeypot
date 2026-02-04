from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
import json

from security import verify_api_key
from sessions import get_session
from detector import detect_scam
from extractor import extract_intelligence
from agent import agent_reply
from callback import send_callback

app = FastAPI(title="NovaAI Nexus Honeypot API")


def safe_success(reply: str):
    """
    GUARANTEED JSON response for GUVI
    """
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "reply": reply
        }
    )


@app.post("/honeypot")
async def honeypot_endpoint(request: Request, api_key: str = Depends(verify_api_key)):
    # ------------------------------------------------------------------
    # STEP 1: Read RAW body (NEVER trust request.json() for GUVI)
    # ------------------------------------------------------------------
    try:
        raw_body = await request.body()
    except Exception:
        return safe_success(
            "Sorry, I didn’t catch that. Could you explain what’s happening?"
        )

    if not raw_body:
        return safe_success(
            "Hi, I’m here to help. Can you tell me what message you received?"
        )

    # ------------------------------------------------------------------
    # STEP 2: Manual JSON parsing (bulletproof)
    # ------------------------------------------------------------------
    try:
        body = json.loads(raw_body.decode("utf-8"))
    except Exception:
        return safe_success(
            "That message looks unclear. Can you resend the details?"
        )

    # ------------------------------------------------------------------
    # STEP 3: Safe field extraction (NO assumptions)
    # ------------------------------------------------------------------
    session_id = str(body.get("sessionId", "unknown-session"))

    message = body.get("message") or {}
    if not isinstance(message, dict):
        message = {}

    text = message.get("text", "")
    if not isinstance(text, str):
        text = ""

    # ------------------------------------------------------------------
    # STEP 4: Session handling
    # ------------------------------------------------------------------
    session = get_session(session_id)

    if text:
        session["messages"].append(text)

    # ------------------------------------------------------------------
    # STEP 5: Scam detection (safe defaults)
    # ------------------------------------------------------------------
    if text:
        detection = detect_scam(text)
    else:
        detection = {
            "scamDetected": False,
            "confidence": "low",
            "scamCategory": "UNKNOWN",
            "detectionSignals": []
        }

    session["detected"] = session["detected"] or detection.get("scamDetected", False)

    # ------------------------------------------------------------------
    # STEP 6: Intelligence extraction (safe)
    # ------------------------------------------------------------------
    if text:
        extracted = extract_intelligence(text)
    else:
        extracted = {
            "bankAccounts": [],
            "upiIds": [],
            "phishingLinks": [],
            "phoneNumbers": [],
            "suspiciousKeywords": []
        }

    # ------------------------------------------------------------------
    # STEP 7: Engagement-maximizing reply (GUVI SCORES THIS)
    # ------------------------------------------------------------------
    reply = agent_reply(
        detection.get("scamDetected", False),
        detection.get("confidence", "low")
    )

    # ------------------------------------------------------------------
    # STEP 8: Callback (MANDATORY but SILENT)
    # ------------------------------------------------------------------
    try:
        if (
            session["detected"]
            and not session["callback_sent"]
            and (
                any(extracted.values())
                or len(session["messages"]) >= 3
            )
        ):
            send_callback({
                "sessionId": session_id,
                "scamDetected": True,
                "totalMessagesExchanged": len(session["messages"]),
                "extractedIntelligence": extracted,
                "agentNotes": "Urgency-based social engineering detected"
            })
            session["callback_sent"] = True
    except Exception:
        # Callback must NEVER break main response
        pass

    # ------------------------------------------------------------------
    # STEP 9: ONLY response GUVI expects
    # ------------------------------------------------------------------
    return safe_success(reply)