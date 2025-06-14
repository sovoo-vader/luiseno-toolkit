# AncestralInvocationEngine – Simulates Ritual Call-and-Response for Spiritual Contact

invocations = {
    "east": {
        "call": "Hiiya tovi! Spirit of rising light, come forward.",
        "response": "I am the dawn-runner. Your path is open."
    },
    "south": {
        "call": "Hema sewaa! Guardian of fire and root, respond.",
        "response": "Flame and seed rise with you. I stand beside."
    },
    "west": {
        "call": "Neya kuma! Waters of memory, return to this place.",
        "response": "The old songs flow. Step into the dream."
    },
    "north": {
        "call": "Oya kinwe! Breath of stone and sky, hear me.",
        "response": "Stillness is yours. The bones remember."
    }
}

def summon(direction):
    chant = invocations.get(direction.lower())
    if not chant:
        return "🔇 No ancestral channel in that direction."
    return f"🗣️ {chant['call']}\n👁️ {chant['response']}"

# Example use
if __name__ == '__main__':
    print(summon("east"))
