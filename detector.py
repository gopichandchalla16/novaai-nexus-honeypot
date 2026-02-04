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

LINK_PATTERNS = [
    r"http[s]?://",
    r"www\."
]


def detect_scam(text: str) -> Dict:
    text_lower = text.lower()
    signals: List[str] = []

    urgency = any(word in text_lower for word in URGENCY_WORDS)
    financial = any(word in text_lower for word in FINANCIAL_WORDS)
    link_present = any(re.search(p, text_lower) for p in LINK_PATTERNS)

    if urgency:
        signals.append("urgency_language")
    if "account" in text_lower:
        signals.append("account_threat")
    if financial:
        signals.append("financial_context")
    if link_present:
        signals.append("external_link")

    scam_detected = urgency and (financial or link_present)

    if urgency and financial and link_present:
        confidence = "high"
    elif urgency and financial:
        confidence = "medium"
    else:
        confidence = "low"

    if "upi" in text_lower:
        category = "UPI_FRAUD"
    elif link_present:
        category = "PHISHING"
    elif "account" in text_lower:
        category = "ACCOUNT_THREAT"
    else:
        category = "SOCIAL_ENGINEERING"

    return {
        "scamDetected": scam_detected,
        "confidence": confidence,
        "scamCategory": category,
        "detectionSignals": signals
    }