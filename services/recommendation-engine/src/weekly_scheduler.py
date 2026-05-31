from datetime import datetime, timedelta

def generate_weekly_schedule(
    subjects,
    weak_subjects=[],
    daily_study_hours=2,
    preferred_start_hour=17
):
    today = datetime.now()
    schedule = []
    for i, subject in enumerate(subjects):
        priority = (
            "high"
            if subject in weak_subjects
            else "normal"
        )
        study_duration = (
            "120 mins"
            if priority == "high"
            else "60 mins"
        )
        revision_duration = (
            "45 mins"
            if priority == "high"
            else "20 mins"
        )
        study_day = (
            today + timedelta(days=i)
        ).strftime("%A")
        test_day = (
            today + timedelta(days=i+1)
        ).strftime("%A")
        schedule.append({
            "subject": subject,
            "priority": priority,
            "study_day": study_day,
            "test_day": test_day,
            "study_duration": study_duration,
            "revision_duration":revision_duration,
            "start_time":f"{preferred_start_hour}:00"
        })

    return schedule