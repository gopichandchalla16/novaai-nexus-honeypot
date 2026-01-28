import os
from fastapi import Header, HTTPException

def verify_api_key(x_api_key: str = Header(...)):
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="API key not configured"
        )

    if x_api_key != api_key:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    return True