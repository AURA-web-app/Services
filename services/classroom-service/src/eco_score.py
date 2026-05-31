def calculate_eco_score(
    occupied,
    noise_level,
    active_devices
):
    score = 100
    if not occupied:
        score += 10
    if noise_level == "High Noise":
        score -= 25

    score -= active_devices * 2
    score = max(0, min(score, 100))

    return {
        "eco_score": score
    }