from fastapi import FastAPI, Depends
import time

from models import RequestModel, ResponseModel, EngagementMetrics, Intelligence
from security import verify_api_key
from sessions import get_session
from detector import detect_scam
from extractor import extract_intelligence
from agent import agent_reply
from callback import send_callback

app = FastAPI(title="NovaAI Nexus Honeypot API")

@app.post("/honeypot", response_model=ResponseModel)
def honeypot_endpoint(req: RequestModel, api_key: str = Depends(verify_api_key)):
    session = get_session(req.sessionId)

    session["messages"].append(req.message.text)

    scam_detected = session["detected"] or detect_scam(req.message.text)
    session["detected"] = scam_detected

    extracted = extract_intelligence(req.message.text)

    metrics = EngagementMetrics(
        engagementDurationSeconds=int(time.time() - session["start_time"]),
        totalMessagesExchanged=len(session["messages"])
    )

    agent_notes = agent_reply(scam_detected, extracted)

    # 🔴 Mandatory GUVI callback — once only
    if scam_detected and not session["callback_sent"] and (
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
        scamDetected=scam_detected,
        engagementMetrics=metrics,
        extractedIntelligence=Intelligence(
            bankAccounts=extracted["bankAccounts"],
            upiIds=extracted["upiIds"],
            phishingLinks=extracted["phishingLinks"]
        ),
        agentNotes=agent_notes
    )