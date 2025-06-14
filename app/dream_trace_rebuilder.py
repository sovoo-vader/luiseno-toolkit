# DreamTraceRebuilder – Tag and Link Dreams to Totems, Motifs, and Functions

dream_index = {
    "owl": {
        "meaning": "hidden knowledge",
        "motif": "vutsierau (enclosing ring)",
        "function": "memory keeper"
    },
    "river": {
        "meaning": "emotional passage",
        "motif": "qaxkwilee (zigzag flow)",
        "function": "ritual cleansing"
    },
    "fire": {
        "meaning": "transformation",
        "motif": "venii-gemaa (flint spark)",
        "function": "soul forge"
    },
    "bear": {
        "meaning": "protection + introspection",
        "motif": "tcwal mila (grounding hand)",
        "function": "dream guardian"
    }
}

def rebuild_trace(symbol):
    s = dream_index.get(symbol.lower())
    if not s:
        return "🌀 No trace data for this dream sign."
    return f"🛌 {symbol.title()} Dream\n🔮 Meaning: {s['meaning']}\n🧶 Motif: {s['motif']}\n🛠️ Function: {s['function']}"

# Example use
if __name__ == '__main__':
    print(rebuild_trace("owl"))
