sessions = {}

def create_session(lead_id, name):
    if lead_id not in sessions:
        sessions[lead_id] = {"name": name}
    return sessions[lead_id]
