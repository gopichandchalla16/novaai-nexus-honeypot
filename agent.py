def agent_reply(scam_detected: bool, extracted: dict) -> str:
    if not scam_detected:
        return (
            "Alright, thanks for letting me know. "
            "Feel free to share more details if needed."
        )

    if not any(extracted.values()):
        return (
            "I want to make sure I understand this correctly. "
            "Could you explain what I’m expected to do next?"
        )

    return (
        "Got it, I’ll look into this. "
        "Let me know if there’s anything else I should be aware of."
    )