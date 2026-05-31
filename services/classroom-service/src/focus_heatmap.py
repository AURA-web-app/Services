import random

def generate_focus_heatmap(student_count):
    heatmap = []
    
    for i in range(student_count):
        focus_score = random.randint(
            40,
            100
        )
        heatmap.append({
            "student_id": i + 1,
            "focus_score": focus_score
        })
    return heatmap