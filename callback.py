import requests

GUVI_CALLBACK_URL = "https://hackathon.guvi.in/api/updateHoneypotFinalResult"

HEADERS = {
    "Content-Type": "application/json"
}

def send_callback(payload: dict):
    try:
        requests.post(
            GUVI_CALLBACK_URL,
            json=payload,
            headers=HEADERS,
            timeout=5
        )
    except Exception:
        pass