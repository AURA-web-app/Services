from datetime import datetime, timedelta

def generate_revision_schedule(topic, mastery_level):
    intervals = {
        "low": [1, 3, 7],
        "medium": [3, 7, 14],
        "high": [7, 14, 30]
    }
    selected = intervals.get(
        mastery_level,
        intervals["medium"]
    )
    today = datetime.now()
    revision_dates = []
    for days in selected:
        revision_dates.append(
            {
                "topic": topic,
                "revision_date":
                (
                    today +
                    timedelta(days=days)
                ).strftime("%Y-%m-%d")
            }
        )
    return revision_dates