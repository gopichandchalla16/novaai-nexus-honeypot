# 🛡️ NovaAI Nexus — Agentic Honeypot for Scam Detection & Intelligence Extraction

NovaAI Nexus is an **Agentic AI Honeypot API** designed for the **India AI Impact Buildathon 2026**, focused on detecting scam messages, autonomously engaging scammers, and extracting actionable intelligence such as UPI IDs, bank accounts, and phishing links — all while following ethical and responsible AI practices.

---

## 🚀 Problem Statement

### **Agentic Honey-Pot for Scam Detection & Intelligence Extraction**

Design an autonomous AI honeypot system that:
- Detects scam messages
- Engages scammers using a believable persona
- Extracts intelligence (UPI IDs, bank accounts, phishing links)
- Returns structured JSON responses
- Ensures ethical AI behavior

---

## ✨ Features

- 🔐 API Key-based Authentication
- 🧠 Scam Detection using Financial Intent + Urgency Logic
- 🤖 Autonomous Agentic Engagement
- 🔍 Intelligence Extraction (UPI, Bank, URLs)
- 📊 Engagement Metrics
- 🔄 GUVI Callback Integration
- 📜 Ethical & Responsible AI Compliance
- ⚡ FastAPI + Modular Architecture

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

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 2️⃣ Activate Environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Server

```bash
uvicorn app:app --reload
```

---

## 🌐 API Access

Open Swagger UI:
```
http://127.0.0.1:8000/docs
```

---

## 🔐 API Authentication

All requests require:

```
x-api-key: YOUR_SECRET_API_KEY
```

Configured inside `security.py`.

---

## 📡 Honeypot Endpoint

### POST `/honeypot`

#### Sample Request

```json
{
  "sessionId": "nova-test-001",
  "message": {
    "sender": "scammer",
    "text": "Send payment to fraudster@upi immediately.",
    "timestamp": "2026-01-21T10:15:00Z"
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  }
}
```

#### Sample Response

```json
{
  "status": "success",
  "scamDetected": true,
  "engagementMetrics": {
    "engagementDurationSeconds": 120,
    "totalMessagesExchanged": 2
  },
  "extractedIntelligence": {
    "bankAccounts": [],
    "upiIds": ["fraudster@upi"],
    "phishingLinks": []
  },
  "agentNotes": "Scam intent confirmed. Agent engaged safely and extracted UPI information."
}
```

---

## 🔁 GUVI Callback Integration

Once scam engagement reaches threshold:

```http
POST https://hackathon.guvi.in/api/updateHoneypotFinalResult
```

Payload includes:
- sessionId
- scamDetected
- extractedIntelligence
- engagement metrics
- agent notes

---

## 🧠 Scam Detection Logic

Triggers scam when:
- Financial intent present
- Urgency or threat language used
- Redirection to payment or links

---

## 🤖 Agent Behavior

The agent:
- Does NOT reveal detection
- Maintains neutral & believable tone
- Asks clarifying questions
- Extracts intelligence safely

---

## 🛡 Ethical AI Compliance

NovaAI Nexus follows:
- No entrapment
- No manipulation
- No victim shaming
- Transparent security design
- Responsible data handling

---

## 🏆 Hackathon Alignment

This project is built according to:

- **India AI Impact Buildathon 2026**
- Problem Statement 2: *Agentic Honey-Pot for Scam Detection & Intelligence Extraction*
- Ethical AI Guidelines
- GUVI API Integration Rules

---

## 📌 Deployment Readiness

✔ Public HTTPS ready  
✔ API secured  
✔ Stateless scalable design  
✔ Always-on compatible  
✔ Free-tier cloud deployable  

---

## 👥 Team

**Team Name:** NovaAI Nexus  
**Event:** India AI Impact Buildathon 2026  
**Organized by:** HCL x GUVI  

---

## 📄 License

This project is for hackathon and educational purposes only.
