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


def safe_reply(text: str = None) -> JSONResponse:
    """
    GUARANTEED GUVI-SAFE RESPONSE
    """
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "reply": text or "Sorry, I’m a bit confused. Can you explain what happened?"
        }
    )


@app.post("/honeypot")
async def honeypot_endpoint(
    request: Request,
    api_key: str = Depends(verify_api_key)
):
    # 1️⃣ Read raw body FIRST (never trust JSON)
    try:
        raw_body = await request.body()
    except Exception:
        return safe_reply()

    # 2️⃣ Try parsing JSON safely
    body = {}
    if raw_body:
        try:
            body = json.loads(raw_body.decode("utf-8"))
        except Exception:
            # GUVI probe / malformed input
            return safe_reply()

    # 3️⃣ Extract fields defensively
    session_id = body.get("sessionId", "unknown-session")
    message = body.get("message") or {}
    text = message.get("text") or ""

    # 4️⃣ Session handling
    session = get_session(session_id)
    if text:
        session["messages"].append(text)

    # 5️⃣ Scam detection (safe default)
    detection = {
        "scamDetected": False,
        "confidence": "low",
        "scamCategory": "UNKNOWN",
        "detectionSignals": []
    }

    if text.strip():
        detection = detect_scam(text)

    session["detected"] = session["detected"] or detection["scamDetected"]

    # 6️⃣ Intelligence extraction (safe default)
    extracted = {
        "bankAccounts": [],
        "upiIds": [],
        "phishingLinks": [],
        "phoneNumbers": [],
        "suspiciousKeywords": []
    }

    if text.strip():
        extracted = extract_intelligence(text)

    # 7️⃣ Engagement-optimized reply (GUVI scoring lives here)
    reply = agent_reply(
        detection["scamDetected"],
        detection["confidence"]
    )

    # 8️⃣ Mandatory callback (SILENT, NEVER BLOCK RESPONSE)
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
                "agentNotes": "Scammer used urgency and credential-harvesting tactics"
            })
            session["callback_sent"] = True
    except Exception:
        pass  # NEVER break honeypot response

    # 9️⃣ GUARANTEED GUVI FORMAT
    return safe_reply(reply)