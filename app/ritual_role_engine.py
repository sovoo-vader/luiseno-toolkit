# RitualRoleEngine – Assign Roles to Ritual Agents Based on Traits and Alignment

roles = {
    "firebearer": {
        "keywords": ["warm", "stable", "resilient"],
        "description": "Carries and maintains sacred fire. Holds center."
    },
    "songkeeper": {
        "keywords": ["vocal", "precise", "lore-bound"],
        "description": "Leads chant rhythms and holds memory-sequence."
    },
    "bonereader": {
        "keywords": ["introspective", "quiet", "seer"],
        "description": "Draws meaning from ashes and signs. Watcher role."
    },
    "circlewalker": {
        "keywords": ["active", "observant", "adaptive"],
        "description": "Walks perimeter, balances energies, detects imbalance."
    },
    "voice_of_the_east": {
        "keywords": ["young", "hopeful", "quick"],
        "description": "Initiates invocation. Opens day-paths."
    }
}

def assign_ritual_role(name, traits):
    scorecard = {}
    for role, data in roles.items():
        score = sum(1 for t in traits if t in data["keywords"])
        scorecard[role] = score
    best = max(scorecard, key=scorecard.get)
    return f"🧍 Agent {name}: {best.replace('_',' ').title()} – {roles[best]['description']}"

# Example use
if __name__ == '__main__':
    print(assign_ritual_role("Ayasha", ["vocal", "lore-bound", "quick"]))
