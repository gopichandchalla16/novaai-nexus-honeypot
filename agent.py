import random

def agent_reply(scam_detected: bool, confidence: str) -> str:
    """
    Engagement-optimized honeypot replies
    Designed to:
    - Sound human
    - Increase reply rate
    - Extract intelligence
    - Avoid detection
    """

    # Stage 1: Innocent confusion (early hook)
    early_confusion = [
        "Sorry, I’m a bit confused. Which account is this about?",
        "I just saw this message. What exactly do I need to do?",
        "I don’t usually get alerts like this. Can you explain?",
        "Is this related to my savings or salary account?"
    ]

    # Stage 2: Urgency compliance (scammer engagement)
    urgency_compliance = [
        "I don’t want my account blocked. What’s the quickest way to fix this?",
        "I’m at work right now. Can this be resolved immediately?",
        "I already verified KYC last year. Why is this happening now?",
        "Please help, I can’t afford any account issues today."
    ]

    # Stage 3: Information probing (intelligence extraction)
    probing = [
        "Should I verify through a link or directly with the bank?",
        "Can you tell me the exact steps so I don’t make a mistake?",
        "Where should I send the verification details?",
        "Is there a reference number for this issue?"
    ]

    # Stage 4: Trust reinforcement (keeps scammer talking)
    trust_building = [
        "I’ve had SBI for years, never faced this before.",
        "This message scared me a bit, please guide me properly.",
        "I just want to make sure I’m doing this the right way."
    ]

    # Confidence-based routing
    if not scam_detected:
        return random.choice(early_confusion)

    if confidence == "low":
        return random.choice(early_confusion + urgency_compliance)

    if confidence == "medium":
        return random.choice(urgency_compliance + probing)

    # High confidence scam → maximize extraction
    return random.choice(probing + trust_building)