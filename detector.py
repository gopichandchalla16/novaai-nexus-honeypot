import re
from typing import Dict, List

URGENCY_WORDS = [
    "urgent", "immediately", "now", "asap",
    "blocked", "suspended", "verify", "action required"
]

FINANCIAL_WORDS = [
    "payment", "transfer", "send", "deposit",
    "upi", "account", "bank", "refund"
]

PHISHING_PATTERNS = [
    r"http[s]?://",
    r"www\.",
    r"\.com",
    r"\.in"
]


def detect_scam(text: str) -> Dict:
    text_lower = text.lower()
    signals: List[str] = []

    urgency = any(w in text_lower for w in URGENCY_WORDS)
    financial = any(w in text_lower for w in FINANCIAL_WORDS)
    phishing = any(re.search(p, text_lower) for p in PHISHING_PATTERNS)

    if urgency:
        signals.append("urgency_language")
    if "account" in text_lower:
        signals.append("account_threat")
    if financial:
        signals.append("payment_redirection")
    if phishing:
        signals.append("phishing_link")

    scam_detected = phishing or (urgency and financial)

    if phishing and urgency and financial:
        confidence = "high"
    elif urgency and financial:
        confidence = "medium"
    else:
        confidence = "low"

    if "upi" in text_lower:
        category = "UPI_FRAUD"
    elif phishing:
        category = "PHISHING"
    elif "account" in text_lower:
        category = "ACCOUNT_THREAT"
    else:
        category = "UNKNOWN"

    return {
        "scamDetected": scam_detected,
        "confidence": confidence,
        "scamCategory": category,
        "detectionSignals": signals
    }