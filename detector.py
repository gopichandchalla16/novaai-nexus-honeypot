import re

URGENCY_WORDS = ["urgent", "immediately", "now", "asap", "blocked", "suspended", "verify"]
FINANCIAL_WORDS = ["payment", "transfer", "send", "deposit", "upi", "account", "bank"]
PHISHING_PATTERNS = [r"http[s]?://", r"www\."]

def detect_scam(text: str) -> bool:
    text_lower = text.lower()

    urgency = any(word in text_lower for word in URGENCY_WORDS)
    financial = any(word in text_lower for word in FINANCIAL_WORDS)
    phishing = any(re.search(pat, text_lower) for pat in PHISHING_PATTERNS)

    # Scam if financial redirection + urgency OR phishing present
    if phishing:
        return True
    if urgency and financial:
        return True

    return False