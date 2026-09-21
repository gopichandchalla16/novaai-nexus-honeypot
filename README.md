<div align="center">

# 🛡️ NovaAI Nexus

### Agentic AI Honeypot for Scam Detection

**India AI Impact Buildathon 2026 · HCL × GUVI**

[![API](https://img.shields.io/badge/API-Live-2EA043?style=for-the-badge)](https://novaai-nexus-honeypot.onrender.com/docs)
[![Python](https://img.shields.io/badge/Python-FastAPI-009688?style=for-the-badge)](https://fastapi.tiangolo.com/)
[![AI](https://img.shields.io/badge/Agentic_AI-Scam_Intelligence-7C3AED?style=for-the-badge)](https://github.com/gopichandchalla16/novaai-nexus-honeypot)

</div>

## 👀 Recruiter Snapshot

NovaAI Nexus is an **agentic AI security system** designed to detect scam messages, engage safely after detection and extract structured intelligence such as UPI IDs, bank accounts and phishing URLs.

### What This Demonstrates

- Agentic AI workflow design
- Scam/phishing signal detection
- Multi-turn session handling
- Structured API design with FastAPI
- Intelligence extraction
- API-key authentication
- Responsible AI constraints
- Public deployment and Swagger documentation

**Live API:** https://novaai-nexus-honeypot.onrender.com/honeypot  
**Swagger:** https://novaai-nexus-honeypot.onrender.com/docs

---

# 🛡️ NovaAI Nexus — Agentic Honeypot for Scam Detection & Intelligence Extraction

NovaAI Nexus is an **Agentic AI Honeypot API** developed for the  
**India AI Impact Buildathon 2026 (HCL x GUVI)**.

The system detects scam messages, safely engages scammers using an autonomous agent, and extracts actionable intelligence such as **UPI IDs, bank accounts, and phishing links**, while strictly following **Responsible AI guidelines**.

---

## 🎯 Selected Problem Statement

### **Problem Statement 2: Agentic Honey-Pot for Scam Detection & Intelligence Extraction**

Design an autonomous AI honeypot system that:

- Detects scam messages
- Autonomously engages scammers after detection
- Maintains multi-turn interaction
- Extracts intelligence (UPI IDs, bank accounts, phishing links)
- Returns structured JSON responses
- Operates ethically without exposing detection logic

**NovaAI Nexus is built specifically for this problem statement.**

---

## ✨ Core Features

- 🔐 API key–based authentication
- 🧠 Scam detection using **financial intent + urgency + phishing signals**
- 🤖 Autonomous agentic engagement
- 🔍 Intelligence extraction (UPI IDs, bank accounts, URLs)
- 📊 Engagement metrics (duration & message count)
- 🧾 Explainable detection rationale
- 🔁 Mandatory GUVI callback integration
- 🛡 Responsible & ethical AI compliance
- ⚡ FastAPI + modular architecture

---

## 📂 Project Structure

```

novaai-nexus-honeypot/
├── app.py              # Main FastAPI application
├── detector.py         # Scam detection logic
├── agent.py            # Autonomous agent responses
├── extractor.py        # Intelligence extraction
├── callback.py         # GUVI callback handler
├── security.py         # API key authentication
├── sessions.py         # Session management
├── models.py           # Request & response schemas
├── config.py           # Configuration
├── requirements.txt    # Dependencies
└── README.md           # Documentation

```

---

## 🌐 Live Deployment

**Public API Endpoint**
```

[https://novaai-nexus-honeypot.onrender.com/honeypot](https://novaai-nexus-honeypot.onrender.com/honeypot)

```

**Swagger Documentation**
```

[https://novaai-nexus-honeypot.onrender.com/docs](https://novaai-nexus-honeypot.onrender.com/docs)

```

---

## 🔐 Authentication

All requests must include the API key:

```

x-api-key: <YOUR_API_KEY>

````

The key is securely validated on every request.

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
````

---

## ✅ JSON Response Schema

```json
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
```

---

## 🧠 Scam Detection Logic

A message is classified as a scam when:

* **Urgency language AND financial intent** are detected
  **OR**
* A **phishing link** is present

This approach ensures:

* Low false positives
* High explainability
* Ethical detection behavior

---

## 🤖 Agentic Engagement Behavior

The autonomous agent:

* Never reveals scam detection
* Never confronts or accuses
* Never requests sensitive information
* Uses neutral, believable language
* Safely prolongs interaction to extract intelligence

---

## 🔁 GUVI Callback Integration

When engagement reaches the defined threshold, the system sends a callback to:

```
POST https://hackathon.guvi.in/api/updateHoneyPotFinalResult
```

Callback payload includes:

* sessionId
* scamDetected
* totalMessagesExchanged
* extractedIntelligence
* agentNotes

Callback failures never interrupt the main API.

---

## 🛡 Responsible AI Compliance

✔ No impersonation

✔ No entrapment

✔ No hallucinated data

✔ No exposure of detection logic

✔ Deterministic & explainable outputs

---

## 🏆 Hackathon Alignment

* **India AI Impact Buildathon 2026**
* Organized by **HCL x GUVI**
* Problem Statement 2: Agentic Honeypot
* Designed for large-scale fraud prevention in India

---

## 🚀 Deployment Readiness

✔ Public HTTPS endpoint

✔ Stable response schema

✔ Secure authentication

✔ Low latency

✔ Always-on compatible

✔ Evaluation-safe

---

## 👥 Team

**Team Name:** NovaAI Nexus
**Event:** India AI Impact Buildathon 2026

---

## 📄 License

This project is developed strictly for hackathon and educational purposes under the India AI Impact Buildathon 2026.
