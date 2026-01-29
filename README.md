# 🛡️ NovaAI Nexus — Agentic Honeypot for Scam Detection & Intelligence Extraction

NovaAI Nexus is a **production-ready Agentic AI Honeypot API** built for the  
**India AI Impact Buildathon 2026 (HCL x GUVI)**.

It detects scam messages, autonomously engages scammers using a safe and believable persona, and extracts actionable intelligence such as **UPI IDs, bank accounts, and phishing links**, while strictly following **Responsible AI principles**.

---

## 🎯 Selected Problem Statement

### **Problem 2: Agentic Honey-Pot for Scam Detection & Intelligence Extraction**

Design an autonomous AI honeypot system that:

- Detects scam messages  
- Engages scammers autonomously after detection  
- Maintains multi-turn conversations  
- Extracts intelligence (UPI IDs, bank accounts, phishing URLs)  
- Returns structured JSON responses  
- Operates ethically without exposing detection  

**NovaAI Nexus is built exclusively for this problem statement.**

---

## ✨ Key Features

- 🔐 API Key–based authentication
- 🧠 Scam detection using **financial intent + urgency + phishing signals**
- 🤖 Autonomous agentic engagement (no human intervention)
- 🔍 Intelligence extraction (UPI IDs, bank accounts, URLs)
- 📊 Engagement metrics (time & message count)
- 🧾 Explainable detection rationale
- 🔁 Mandatory GUVI callback integration
- 🛡 Responsible & ethical AI compliance
- ⚡ FastAPI + modular architecture

---

## 📂 Project Structure

```
novaai-nexus-honeypot/
├── app.py              # Main FastAPI app
├── detector.py         # Scam detection logic
├── agent.py            # Autonomous agent responses
├── extractor.py        # Intelligence extraction
├── callback.py         # GUVI callback handler
├── security.py         # API key authentication
├── sessions.py         # Session management
├── models.py           # Request & Response schemas
├── config.py           # Configuration file
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
```

---

## 🌐 Live Deployment

**Public API Endpoint**

https://novaai-nexus-honeypot.onrender.com/honeypot

**Swagger Documentation**

https://novaai-nexus-honeypot.onrender.com/docs

---

## 🔐 Authentication

All requests require an API key:

x-api-key: <YOUR_API_KEY>


The API key is securely read from environment variables and validated on every request.

---

## 📡 Honeypot API Endpoint

### **POST /honeypot**

### Sample Request

```json
{
  "sessionId": "test-phishing-001",
  "message": {
    "sender": "scammer",
    "text": "Your KYC is incomplete. Update immediately at https://secure-verify-now.com",
    "timestamp": "2026-02-01T10:10:00Z"
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  }
}

✅ Response Schema (Evaluation-Ready)
{
  "status": "success",
  "scamDetected": true,
  "engagementMetrics": {
    "engagementDurationSeconds": 148,
    "totalMessagesExchanged": 3
  },
  "extractedIntelligence": {
    "bankAccounts": [],
    "upiIds": ["fraudster@upi"],
    "phishingLinks": ["https://secure-verify-now.com"]
  },
  "agentNotes": "I want to make sure I understand this correctly. Could you explain what I’m expected to do next?",
  "agentExplanation": {
    "confidence": "low",
    "scamCategory": "PHISHING",
    "detectionSignals": [
      "urgency_language",
      "phishing_link"
    ],
    "recommendedAction": "Avoid sharing sensitive information and report this interaction through official channels.",
    "systemRationale": "Designed to safely engage scammers while gathering evidence without exposing detection."
  }
}

🧠 Scam Detection Logic

A message is classified as a scam when:

Urgency language AND financial intent are detected
OR

A phishing link is present

This approach ensures:

Low false positives

High explainability

Ethical detection

🤖 Agentic Engagement Behavior

The autonomous agent:

Never reveals scam detection

Never confronts or accuses

Never requests sensitive information

Uses neutral, believable language

Safely prolongs conversation to extract intelligence

🔁 GUVI Callback Integration

When engagement reaches threshold:

POST https://hackathon.guvi.in/api/updateHoneyPotFinalResult


Callback payload includes:

sessionId

scamDetected

totalMessagesExchanged

extractedIntelligence

agentNotes

Callback failures never interrupt the main API.

🛡 Responsible AI Compliance

✔ No impersonation
✔ No entrapment
✔ No hallucinated data
✔ No exposure of detection logic
✔ Deterministic & explainable outputs

🏆 Hackathon Alignment

India AI Impact Buildathon 2026

Organized by HCL x GUVI

Problem Statement 2: Agentic Honeypot

Designed for large-scale fraud prevention in India

🚀 Deployment Readiness

✔ Public HTTPS endpoint
✔ Stable response schema
✔ Secure authentication
✔ Low latency
✔ Always-on compatible
✔ Evaluation-safe

👥 Team

Team Name: NovaAI Nexus
Event: India AI Impact Buildathon 2026

📄 License

This project is developed strictly for hackathon and educational purposes under the India AI Impact Buildathon 2026.
