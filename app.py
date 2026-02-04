from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time

from security import verify_api_key
from sessions import get_session
from detector import detect_scam
from extractor import extract_intelligence
from agent import agent_reply
from callback import send_callback

app = FastAPI(title="NovaAI Nexus Honeypot API")


@app.post("/honeypot")
async def honeypot_endpoint(request: Request):
    """
    GUVI-compliant honeypot endpoint
    - ALWAYS returns JSON
    - NEVER throws errors
    - NEVER returns HTML
    """

    # Default safe reply (used if anything fails)
    safe_response = {
        "status": "success",
        "reply": "Sorry, I didn’t understand that. Can you explain again?"
    }

    try:
        # --- API KEY CHECK (NEVER FAIL HARD) ---
        try:
            await verify_api_key(request)
        except Exception:
            return JSONResponse(status_code=200, content=safe_response)

        # --- PARSE BODY SAFELY ---
        try:
            body = await request.json()
        except Exception:
            return JSONResponse(status_code=200, content=safe_response)

        session_id = body.get("sessionId", "unknown-session")
        message = body.get("message") or {}
        text = message.get("text") or ""

        # --- SESSION ---
        session = get_session(session_id)
        if text:
            session["messages"].append(text)

        # --- DETECTION (SAFE) ---
        try:
            detection = detect_scam(text) if text else {
                "scamDetected": False,
                "confidence": "low"
            }
        except Exception:
            detection = {
                "scamDetected": False,
                "confidence": "low"
            }

        session["detected"] = session["detected"] or detection.get("scamDetected", False)

        # --- EXTRACTION (SAFE) ---
        try:
            extracted = extract_intelligence(text) if text else {}
        except Exception:
            extracted = {}

        # --- AGENT REPLY (ENGAGEMENT-SCORED) ---
        try:
            reply = agent_reply(
                detection.get("scamDetected", False),
                detection.get("confidence", "low")
            )
        except Exception:
            reply = safe_response["reply"]

        # --- CALLBACK (SILENT, NEVER BLOCKS) ---
        try:
            if session["detected"] and not session["callback_sent"] and (
                extracted or len(session["messages"]) >= 3
            ):
                send_callback({
                    "sessionId": session_id,
                    "scamDetected": True,
                    "totalMessagesExchanged": len(session["messages"]),
                    "extractedIntelligence": extracted,
                    "agentNotes": "Urgency-based scam with credential harvesting behavior"
                })
                session["callback_sent"] = True
        except Exception:
            pass  # NEVER let callback affect response

        # --- FINAL GUVI RESPONSE ---
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "reply": reply
            }
        )

    except Exception:
        # Absolute last-resort guard
        return JSONResponse(status_code=200, content=safe_response)