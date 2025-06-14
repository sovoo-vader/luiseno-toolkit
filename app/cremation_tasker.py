# CremationTasker – Burn Task Objects Until Heart (Final Component) is Consumed

import time
import random

class RitualTask:
    def __init__(self, name, steps):
        self.name = name
        self.steps = steps
        self.burnt = []

    def rotate_and_burn(self):
        print(f"\n🔥 Beginning Cremation Ritual for '{self.name}'")
        for i, step in enumerate(self.steps):
            time.sleep(0.3)
            print(f"Turning {step} into flame...", end=' ')
            if step.lower() == "heart":
                print("💀 FINAL HEART BURNED")
                self.burnt.append(step)
                break
            print("done.")
            self.burnt.append(step)
        print(f"🔥 Ritual complete: {self.burnt}\n")

# Example usage
if __name__ == '__main__':
    task = RitualTask("MemoryFlush-v1", ["head", "limbs", "torso", "heart"])
    task.rotate_and_burn()
