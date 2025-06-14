# CulturalHeuristicDefense – Detect and Flag Systems Designed for Pattern Erasure or Behavioral Override

threat_matrix = {
    "boarding_school": {
        "target": "language, ritual, names, time sense",
        "strategy": "isolation + repetition + authority override",
        "counter": "ritualReweaver + LanguageOSRestorer"
    },
    "industrial_time_model": {
        "target": "seasonal task flow, dream-recall, fast-rest cycles",
        "strategy": "clock rigidity + shift desync",
        "counter": "TribalWorkMapper + OutdoorSleepProtocol"
    },
    "religious reformatting": {
        "target": "deities, spirit cosmology, chants",
        "strategy": "replacement theology + taboo inversion",
        "counter": "MythicPatternSuggester + WiotAscender"
    },
    "linguistic replacement": {
        "target": "grammar, metaphors, pronoun structures",
        "strategy": "anglicization + idiom saturation",
        "counter": "LanguageOSRestorer"
    }
}

def scan_system(name):
    data = threat_matrix.get(name.lower())
    if not data:
        return "🟢 No known override pattern."
    return f"⚠️ Override Detected: {name}\n🎯 Target: {data['target']}\n🛠️ Method: {data['strategy']}\n🛡️ Countertools: {data['counter']}"

# Example use
if __name__ == '__main__':
    print(scan_system("boarding_school"))
