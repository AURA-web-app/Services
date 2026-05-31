from logger import logs

def generate_metrics():
    total_logs = len(logs)

    ai_requests = len([
        log for log in logs
        if log["event_type"] == "ai_request"
    ])

    provider_failures = len([
        log for log in logs
        if log["event_type"] == "provider_failure"
    ])

    sms_requests = len([
        log for log in logs
        if log["event_type"] == "sms_request"
    ])

    return {
        "total_logs": total_logs,
        "ai_requests": ai_requests,
        "provider_failures": provider_failures,
        "sms_requests": sms_requests
    }