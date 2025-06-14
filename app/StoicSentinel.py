# StoicSentinel – Monitors Text for Emotional Leakage and Advises Restraint

import re

def scan_emotion(text):
    if re.search(r"(i hate|i can't|it's hopeless|what's the point|i give up|so unfair)", text, re.IGNORECASE):
        return "🧘 StoicSentinel: 'No repining.' Refocus breath. Accept and act."
    return "✅ Steady path. No correction needed."

if __name__ == '__main__':
    sample_input = "I can't believe how unfair everything is right now."
    print(scan_emotion(sample_input))
