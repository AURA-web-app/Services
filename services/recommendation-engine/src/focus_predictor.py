def predict_focus(
    study_minutes,
    distraction_count,
    consistency_score
):
    focus_score = (
        study_minutes * 0.4
        +
        consistency_score * 0.5
        -
        distraction_count * 5
    )
    if focus_score >= 80:
        level = "Excellent"
    elif focus_score >= 50:
        level = "Moderate"
    else:
        level = "Poor"

    return {
        "focus_score": round(focus_score, 2),
        "level": level
    }