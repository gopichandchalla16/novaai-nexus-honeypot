def agent_reply(scam_detected: bool, extracted: dict) -> str:
    if not scam_detected:
        return "Alright, let me know if there’s anything you’d like me to check."

    # Scam detected but no intelligence extracted yet
    if not any(extracted.values()):
        return (
            "I’m not fully clear on this yet. Could you explain how I’m supposed to proceed?"
        )

    # Some intelligence already extracted
    return (
        "Got it, I’ll look into this. Is there anything else I should be aware of?"
    )