# NasalBreathTrainer – Train and Monitor Breath Discipline with Real-Time Feedback
import time
import random

def simulate_breath_cycle():
    states = ["inhale (nose)", "exhale (nose)", "inhale (mouth)", "exhale (mouth)"]
    current = random.choice(states)
    print(f"👃 Breath State: {current}")
    if "mouth" in current:
        print("⚠️ Alert: Recalibrate to nasal breathing.")
    else:
        print("✅ Stable nasal pattern.")

if __name__ == '__main__':
    for _ in range(5):
        time.sleep(1)
        simulate_breath_cycle()
