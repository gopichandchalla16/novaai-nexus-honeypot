def agent_reply(scam_detected: bool, confidence: str) -> str:
    """
    Top-10 engagement honeypot strategy.

    Goals:
    - Keep the scammer talking longer
    - Extract bank name, process, link, urgency signals
    - Sound anxious but cooperative
    - Never warn or confront the scammer
    """

    # -------------------------------------------------
    # NO SCAM DETECTED / UNCLEAR MESSAGE
    # -------------------------------------------------
    if not scam_detected:
        return (
            "Hi, I’m a bit confused about this message. "
            "Could you explain what it’s regarding?"
        )

    # -------------------------------------------------
    # LOW CONFIDENCE SCAM
    # Early hook: innocent confusion
    # -------------------------------------------------
    if confidence == "low":
        return (
            "Sorry, I just noticed this message. "
            "Which account is this related to?"
        )

    # -------------------------------------------------
    # MEDIUM CONFIDENCE SCAM
    # Urgency + compliance
    # -------------------------------------------------
    if confidence == "medium":
        return (
            "That sounds serious. I don’t want any account issues. "
            "What exactly do I need to do to fix this?"
        )

    # -------------------------------------------------
    # HIGH CONFIDENCE SCAM
    # Maximum intelligence extraction
    # -------------------------------------------------
    return (
        "I’m getting worried now. I’ve never faced this before. "
        "Can you tell me the exact steps and where I need to verify?"
    )