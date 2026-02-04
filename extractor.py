import re
from typing import Dict, List

BANK_KEYWORDS = [
    "sbi", "hdfc", "icici", "axis", "kotak",
    "bank", "upi", "paytm", "gpay", "phonepe"
]

URGENCY_KEYWORDS = [
    "urgent", "immediately", "today", "now",
    "blocked", "suspended", "verify", "action required"
]

ATTACK_PATTERNS = {
    "account_threat": ["blocked", "suspended", "freeze"],
    "credential_harvest": ["verify", "update", "confirm"],
    "payment_redirection": ["send", "transfer", "pay"]
}


def extract_intelligence(text: str) -> Dict:
    """
    Extracts structured scam intelligence for GUVI callback.
    Designed for clarity, not over-engineering.
    """

    text_lower = text.lower()

    bank_accounts = re.findall(r"\b\d{9,18}\b", text)
    upi_ids = re.findall(r"\b[\w.-]+@[\w.-]+\b", text)
    phishing_links = re.findall(r"https?://\S+", text)

    impersonated_bank = None
    for bank in BANK_KEYWORDS:
        if bank in text_lower:
            impersonated_bank = bank.upper()
            break

    urgency_indicators = [
        word for word in URGENCY_KEYWORDS if word in text_lower
    ]

    attack_tactics: List[str] = []
    for tactic, keywords in ATTACK_PATTERNS.items():
        if any(k in text_lower for k in keywords):
            attack_tactics.append(tactic)

    return {
        "bankAccounts": bank_accounts,
        "upiIds": upi_ids,
        "phishingLinks": phishing_links,
        "impersonatedBank": impersonated_bank,
        "urgencyIndicators": urgency_indicators,
        "attackTactics": attack_tactics,
        "messageSample": text[:120] + "..." if len(text) > 120 else text
    }