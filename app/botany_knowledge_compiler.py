# BotanyKnowledgeCompiler – Encodes Plant Timing, Symbolism, and Function

plant_lore = {
    "redbud": {
        "season": "spring",
        "use": "color striping",
        "symbol": "vitality and ancestral memory",
        "note": "harvest after bud flashes but before bark loosens"
    },
    "willow": {
        "season": "late winter",
        "use": "structural coil",
        "symbol": "flexibility, lineage path",
        "note": "cut before sap rise to preserve strength"
    },
    "fern": {
        "season": "early summer",
        "use": "dark accent",
        "symbol": "mourning and moon rituals",
        "note": "collect once stem glosses; avoid rust"
    },
    "sumach": {
        "season": "autumn",
        "use": "fiery dye",
        "symbol": "protection and cleansing",
        "note": "boil bark infusion for color"
    }
}

def lookup_plant(name):
    data = plant_lore.get(name.lower())
    if not data:
        return f"Unknown plant '{name}'."
    return f"🌿 {name.title()} – Season: {data['season']}, Use: {data['use']}, Symbol: {data['symbol']}, Note: {data['note']}"

# Example use
if __name__ == '__main__':
    print(lookup_plant("fern"))
