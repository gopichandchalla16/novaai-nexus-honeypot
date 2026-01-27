import os

API_KEY = os.getenv("API_KEY")
GUVI_CALLBACK_URL = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"

if not API_KEY:
    raise RuntimeError("API_KEY environment variable is not set")