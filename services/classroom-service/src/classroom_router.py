from occupancy_detector import (
    detect_occupancy
)

from noise_analyzer import (
    analyze_noise
)

from eco_score import (
    calculate_eco_score
)

from focus_heatmap import (
    generate_focus_heatmap
)

def run_classroom_analysis():
    occupancy_data = detect_occupancy()
    noise_data = analyze_noise()
    eco = calculate_eco_score(
        occupied = occupancy_data["occupied"],
        noise_level = noise_data["noise_level"],
        active_devices = 5
    )
    heatmap = generate_focus_heatmap(occupancy_data["count"])

    return {
        "occupancy": occupancy_data,
        "noise": noise_data,
        "eco_score": eco["eco_score"],
        "focus_heatmap": heatmap
    }