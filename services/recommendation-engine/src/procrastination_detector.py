from datetime import datetime

def detect_procrastination(
    assigned_date,
    completed_date,
    allowed_days=2
):
    assigned = datetime.strptime(
        assigned_date,
        "%Y-%m-%d"
    )
    completed = datetime.strptime(
        completed_date,
        "%Y-%m-%d"
    )
    delta = (
        completed - assigned
    ).days
    if delta > allowed_days:
        return {
            "procrastinating": True,
            "delay_days": delta
        }
    return {
        "procrastinating": False,
        "delay_days": delta
    }