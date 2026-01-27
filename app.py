from fastapi import FastAPI, Depends
from models import RequestModel, ResponseModel, EngagementMetrics, Intelligence
from security import verify_api_key
from sessions import get_session
from detector import detect_scam
from extractor import extract_intelligence
from agent import agent_reply
from callback import send_callback
import time

app = FastAPI(title="NovaAI Nexus Honeypot API")

@app.post("/honeypot", response_model=ResponseModel)
def honeypot_endpoint(req: RequestModel, api_key: str = Depends(verify_api_key)):
    session = get_session(req.sessionId)

    # Track messages
    session["messages"].append(req.message.text)

    # Detect scam conservatively
    scamDetected = session["detected"] or detect_scam(req.message.text)
    session["detected"] = scamDetected

    # Extract intelligence
    extracted = extract_intelligence(req.message.text)

    # Update metrics
    metrics = EngagementMetrics(
        engagementDurationSeconds=int(time.time() - session["start_time"]),
        totalMessagesExchanged=len(session["messages"])
    )

    # Generate agent response
    agent_notes = agent_reply(scamDetected, extracted)

    # Mandatory callback when scam confirmed AND engagement complete
    if scamDetected and (any(extracted.values()) or metrics.totalMessagesExchanged >= 3):
        send_callback({
            "sessionId": req.sessionId,
            "scamDetected": True,
            "totalMessagesExchanged": metrics.totalMessagesExchanged,
            "extractedIntelligence": {
                "bankAccounts": extracted["bankAccounts"],
                "upiIds": extracted["upiIds"],
                "phishingLinks": extracted["phishingLinks"],
                "phoneNumbers": [],
                "suspiciousKeywords": []
            },
            "agentNotes": agent_notes
        })

    return ResponseModel(
        status="success",
        scamDetected=scamDetected,
        engagementMetrics=metrics,
        extractedIntelligence=Intelligence(
            bankAccounts=extracted["bankAccounts"],
            upiIds=extracted["upiIds"],
            phishingLinks=extracted["phishingLinks"]
        ),
        agentNotes=agent_notes
    )