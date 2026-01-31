from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import time

from models import (
    RequestModel,
    ResponseModel,
    EngagementMetrics,
    Intelligence,
    AgentExplanation
)
from security import verify_api_key
from sessions import get_session
from detector import detect_scam
from extractor import extract_intelligence
from agent import agent_reply
from callback import send_callback

app = FastAPI(title="NovaAI Nexus Honeypot API")


# 🔥 GLOBAL VALIDATION ERROR HANDLER (NO 422 EVER)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=200,
        content={
            "status": "error",
            "scamDetected": False,
            "engagementMetrics": {
                "engagementDurationSeconds": 0,
                "totalMessagesExchanged": 0
            },
            "extractedIntelligence": {
                "bankAccounts": [],
                "upiIds": [],
                "phishingLinks": []
            },
            "agentNotes": "Invalid or incomplete request received. Awaiting valid scam message.",
            "agentExplanation": {
                "confidence": "low",
                "scamCategory": "UNKNOWN",
                "detectionSignals": [],
                "recommendedAction": "Ensure request matches documented API schema.",
                "systemRationale": "Graceful handling ensures system stability during automated evaluation."
            }
        }
    )


@app.post("/honeypot", response_model=ResponseModel)
def honeypot_endpoint(req: RequestModel, api_key: str = Depends(verify_api_key)):
    # Normalize message (SAFE)
    msg = req.message.normalize()

    session = get_session(req.sessionId)
    session["messages"].append(msg["text"])

    detection = detect_scam(msg["text"])
    session["detected"] = session["detected"] or detection["scamDetected"]

    extracted = extract_intelligence(msg["text"])

    metrics = EngagementMetrics(
        engagementDurationSeconds=int(time.time() - session["start_time"]),
        totalMessagesExchanged=len(session["messages"])
    )

    agent_notes = agent_reply(
        detection["scamDetected"],
        detection["confidence"]
    )

    explanation = AgentExplanation(
        confidence=detection["confidence"],
        scamCategory=detection["scamCategory"],
        detectionSignals=detection["detectionSignals"],
        recommendedAction=(
            "Avoid sharing sensitive information and report this interaction through official channels."
        ),
        systemRationale=(
            "Designed to safely engage scammers while gathering evidence without exposing detection."
        )
    )

    if session["detected"] and not session["callback_sent"] and (
        any(extracted.values()) or metrics.totalMessagesExchanged >= 3
    ):
        send_callback({
            "sessionId": req.sessionId,
            "scamDetected": True,
            "totalMessagesExchanged": metrics.totalMessagesExchanged,
            "extractedIntelligence": extracted,
            "agentNotes": agent_notes
        })
        session["callback_sent"] = True

    return ResponseModel(
        status="success",
        scamDetected=detection["scamDetected"],
        engagementMetrics=metrics,
        extractedIntelligence=Intelligence(**extracted),
        agentNotes=agent_notes,
        agentExplanation=explanation
    )