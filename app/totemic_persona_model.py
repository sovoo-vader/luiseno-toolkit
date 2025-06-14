# TotemicPersonaModel – Build a Cognitive-Emotional Agent Model from Totem Archetype

totem_templates = {
    "bear": {
        "traits": ["protective", "introspective", "steady"],
        "default_motive": "guard memory and boundary",
        "response_pattern": "slow, low, precise"
    },
    "coyote": {
        "traits": ["disruptive", "clever", "unexpected"],
        "default_motive": "test structure for weakness",
        "response_pattern": "shift, laugh, evade"
    },
    "owl": {
        "traits": ["observant", "quiet", "knowing"],
        "default_motive": "illuminate hidden links",
        "response_pattern": "pause, speak once"
    },
    "eagle": {
        "traits": ["visionary", "swift", "commanding"],
        "default_motive": "guide arc of group",
        "response_pattern": "rise, scan, signal"
    }
}

class TotemicAgent:
    def __init__(self, name, totem):
        base = totem_templates.get(totem.lower())
        if not base:
            raise ValueError("Unknown totem")
        self.name = name
        self.totem = totem
        self.traits = base["traits"]
        self.motive = base["default_motive"]
        self.pattern = base["response_pattern"]

    def describe(self):
        print(f"🌐 {self.name} as {self.totem.title()} Totem")
        print(f"Traits: {', '.join(self.traits)}")
        print(f"Motive: {self.motive}")
        print(f"Pattern: {self.pattern}")

# Example use
if __name__ == '__main__':
    agent = TotemicAgent("Mika", "Owl")
    agent.describe()
