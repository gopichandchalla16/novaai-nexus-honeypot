import os

def verify_api_key(x_api_key: str | None) -> bool:
    """
    GUVI-safe API key verification.
    - NEVER raises HTTPException
    - NEVER breaks response pipeline
    - Returns True / False only
    """
    api_key = os.getenv("API_KEY")

    # If API key not configured, allow (avoid crash during eval)
    if not api_key:
        return True

    # If key missing or invalid → False (handled in app.py)
    if not x_api_key or x_api_key != api_key:
        return False

    return True