# CeremonialHomeConstructor – Generate Layouts Based on Tribe, Ritual Use, and Terrain

layout_index = {
    ("luiseño", "mourning", "valley"): {
        "centerpiece": "low stone ring with burning coals",
        "entrance": "east-facing shadow path",
        "sleep_zone": "north edge under willow arch",
        "sacred_area": "circle of woven mats for ancestor dreams"
    },
    ("hopi", "vision", "mesa"): {
        "centerpiece": "sun-marked sand spiral",
        "entrance": "northeast for rising clarity",
        "sleep_zone": "near western kiva wall",
        "sacred_area": "corner clay mound with feathers"
    },
    ("yurok", "healing", "river"): {
        "centerpiece": "bundle of roots wrapped in red thread",
        "entrance": "south gate for water spirit access",
        "sleep_zone": "upwind near cedar split",
        "sacred_area": "fern-ringed basin for herbal steam"
    }
}

def generate_layout(tribe, purpose, terrain):
    key = (tribe.lower(), purpose.lower(), terrain.lower())
    data = layout_index.get(key)
    if not data:
        return "🛖 No ceremonial template available."
    layout = f"🏕️ Layout for {tribe.title()} ({purpose}) in {terrain} terrain:\n"
    layout += f"• 🔥 Centerpiece: {data['centerpiece']}\n"
    layout += f"• 🚪 Entrance: {data['entrance']}\n"
    layout += f"• 🛏️ Sleep Zone: {data['sleep_zone']}\n"
    layout += f"• 🌀 Sacred Area: {data['sacred_area']}"
    return layout

# Example use
if __name__ == '__main__':
    print(generate_layout("Luiseño", "mourning", "valley"))
