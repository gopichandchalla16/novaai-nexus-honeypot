# NovaAI Nexus – Agentic Honeypot for Scam Detection

An AI-powered **Agentic Honeypot API** built for the **India AI Impact Buildathon 2026 (GUVI × HCL)** to detect scam messages and autonomously extract scam intelligence.

This system detects scam intent, engages scammers using a human-like AI agent, and extracts actionable intelligence such as UPI IDs, bank accounts, and phishing links.

---

## 🚀 Features

- Scam message detection  
- Autonomous AI agent engagement  
- Multi-turn conversation support  
- Intelligence extraction:
  - UPI IDs  
  - Bank accounts  
  - Phishing links  
- Secured with `x-api-key`  
- Structured JSON responses  
- Mandatory GUVI callback supported  
- Production-ready FastAPI service  

---

## 🧩 Tech Stack

- Python 3.9+
- FastAPI
- Uvicorn
- Pydantic

---

## 📂 Project Structure

novaai-nexus-honeypot/
│
├── app.py # Main API
├── detector.py # Scam detection logic
├── agent.py # AI agent responses
├── extractor.py # Intelligence extraction
├── callback.py # GUVI callback sender
├── security.py # API key validation
├── sessions.py # Session management
├── models.py # Request/response schemas
├── config.py # Configuration
├── requirements.txt
└── README.md


---

## 🔐 API Security

All requests must include:

x-api-key: YOUR_SECRET_API_KEY

Requests without a valid API key are rejected.

---

## 📥 API Endpoint

### POST `/honeypot`

Accepts scam message events and returns analysis.

### Example Request

```json
{
  "sessionId": "test-001",
  "message": {
    "sender": "scammer",
    "text": "Your account is blocked. Verify now.",
    "timestamp": "2026-01-21T10:15:30Z"
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  
Example Response

{
  "status": "success",
  "scamDetected": true,
  "engagementMetrics": {
    "engagementDurationSeconds": 120,
    "totalMessagesExchanged": 3
  },
  "extractedIntelligence": {
    "bankAccounts": [],
    "upiIds": ["fraud@upi"],
    "phishingLinks": []
  },
  "agentNotes": "Scam intent confirmed through urgency and payment redirection language. Agent engaged safely and extracted UPI information without exposing detection."
}

⚙️ Setup Instructions
1️⃣ Create virtual environment

python -m venv venv
venv\Scripts\activate

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Run the server

uvicorn app:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

📤 GUVI Final Callback

Once scam engagement completes, the system sends extracted intelligence to:

POST https://hackathon.guvi.in/api/updateHoneyPotFinalResult
This is mandatory for evaluation.

🏆 Hackathon Alignment

This project is built according to:

India AI Impact Buildathon

Problem Statement 2: Agentic Honey-Pot for Scam Detection & Intelligence Extraction

GUVI document reference

Ethical AI guidelines

👨‍💻 Team

Team Name: NovaAI Nexus
Event: India AI Impact Buildathon 2026
Organized by: HCL × GUVI