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

# -------------------------------------------------
# ALWAYS return JSON (GUVI rule)
# -------------------------------------------------
def safe_success(reply: str):
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "reply": reply
        }
    )

# -------------------------------------------------
# HANDLE ALL METHODS (POST / GET / OPTIONS / HEAD)
# -------------------------------------------------
@app.api_route("/honeypot", methods=["POST", "GET", "OPTIONS", "HEAD"])
async def honeypot(request: Request, api_key: str = Depends(verify_api_key)):

    # ---- Non-POST requests (GUVI preflight, health, probing)
    if request.method != "POST":
        return safe_success(
            "Hi, I’m here to help. Can you tell me what message you received?"
        )

    # ---- Read raw body safely
    try:
        raw_body = await request.body()
    except Exception:
        return safe_success(
            "I couldn’t read the message clearly. Can you explain what happened?"
        )

    if not raw_body:
        return safe_success(
            "Hi, I’m here to help. What message did you receive?"
        )

    # ---- Parse JSON manually (NO request.json())
    try:
        body = json.loads(raw_body.decode("utf-8"))
    except Exception:
        return safe_success(
            "That message looks unclear. Can you resend the details?"
        )

    # ---- Extract fields defensively
    session_id = str(body.get("sessionId", "unknown-session"))

    message = body.get("message", {})
    if not isinstance(message, dict):
        message = {}

    text = message.get("text", "")
    if not isinstance(text, str):
        text = ""

    # ---- Session
    session = get_session(session_id)
    if text:
        session["messages"].append(text)

    # ---- Detection
    if text:
        detection = detect_scam(text)
    else:
        detection = {
            "scamDetected": False,
            "confidence": "low"
        }

    session["detected"] = session["detected"] or detection.get("scamDetected", False)

    # ---- Extraction
    extracted = extract_intelligence(text) if text else {}

    # ---- Engagement reply (scored by GUVI)
    reply = agent_reply(
        detection.get("scamDetected", False),
        detection.get("confidence", "low")
    )

    # ---- Callback (silent, never break response)
    try:
        if (
            session["detected"]
            and not session["callback_sent"]
            and (extracted or len(session["messages"]) >= 3)
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
        pass

    # ---- FINAL RESPONSE (ONLY THIS)
    return safe_success(reply)

# -------------------------------------------------
# Root health (GUVI sometimes checks this)
# -------------------------------------------------
@app.get("/")
async def root():
    return safe_success("Honeypot API is running.")