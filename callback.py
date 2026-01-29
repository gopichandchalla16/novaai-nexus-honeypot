import requests

GUVI_CALLBACK_URL = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"

def send_callback(payload: dict):
    try:
        requests.post(GUVI_CALLBACK_URL, json=payload, timeout=5)
    except Exception:
        pass