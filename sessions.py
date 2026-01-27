from collections import defaultdict
import time

sessions = defaultdict(dict)

def get_session(session_id):
    if session_id not in sessions:
        sessions[session_id] = {
            "start_time": time.time(),
            "messages": [],
            "detected": False
        }
    return sessions[session_id]