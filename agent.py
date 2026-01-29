def agent_reply(scam_detected: bool, confidence: str) -> str:
    if not scam_detected:
        return (
            "Alright, thanks for letting me know. "
            "Feel free to share more details if needed."
        )

    if confidence == "high":
        return (
            "Okay, I’ll take a look at this. "
            "Let me know if there’s anything else I should be aware of."
        )

    return (
        "I want to make sure I understand this correctly. "
        "Could you explain what I’m expected to do next?"
    )