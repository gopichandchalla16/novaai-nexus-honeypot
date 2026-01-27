import re

def extract_intelligence(text: str):
    return {
        "bankAccounts": re.findall(r"\b\d{9,18}\b", text),
        "upiIds": re.findall(r"\b[\w.-]+@[\w.-]+\b", text),
        "phishingLinks": re.findall(r"https?://\S+", text),
        "phoneNumbers": re.findall(r"\+91\d{10}", text),
        "suspiciousKeywords": [w for w in ["urgent", "verify", "blocked", "suspend", "limited"] if w in text.lower()]
    }