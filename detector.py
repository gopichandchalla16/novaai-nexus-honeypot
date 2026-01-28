import re

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

def detect_scam(text: str) -> bool:
    """
    Conservative scam detection:
    - Financial intent + urgency
    - OR phishing link presence
    """
    text_lower = text.lower()

    urgency = any(word in text_lower for word in URGENCY_WORDS)
    financial = any(word in text_lower for word in FINANCIAL_WORDS)
    phishing = any(re.search(pat, text_lower) for pat in PHISHING_PATTERNS)

    if phishing:
        return True

    if urgency and financial:
        return True

    return False