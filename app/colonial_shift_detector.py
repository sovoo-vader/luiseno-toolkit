# ColonialShiftDetector – Identify Cultural Displacement in Text by Lexical Triggers

import re

shift_keywords = [
    "mission", "school", "conversion", "Christian", "soldier",
    "forbidden", "punished", "replaced", "forced", "language"
]

def detect_colonial_shifts(text):
    sentences = re.split(r'[.!?]', text)
    shifts = []
    for s in sentences:
        if any(k in s.lower() for k in shift_keywords):
            shifts.append(s.strip())
    return shifts or ["None"]

# Example
if __name__ == '__main__':
    sample = "They were forbidden to speak their language. Soldiers came and forced them into schools."
    print("🚫 Colonial Shift Phrases:")
    for line in detect_colonial_shifts(sample):
        print(f" - {line}")