import sounddevice as sd
import numpy as np

def analyze_noise():
    duration = 2
    sample_rate = 44100
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1
    )
    sd.wait()
    volume = np.linalg.norm(recording)
    db_estimate = round(volume * 10, 2)
    
    if db_estimate > 70:
        level = "High Noise"
    elif db_estimate > 40:
        level = "Moderate"
    else:
        level = "Low"

    return {
        "db_estimate": db_estimate,
        "noise_level": level
    }