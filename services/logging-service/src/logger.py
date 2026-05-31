from datetime import datetime

logs = []

def log_event(
    event_type,
    metadata={}
):
    log = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "metadata": metadata
    }
    logs.append(log)
    return log