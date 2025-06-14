# CulturalContextLinker – Link Practices to Ethnographic or Environmental Metadata

import re

context_map = {
    "acorn": "Harvested and leached as staple food; stored in granaries",
    "fire": "Used in rituals, cooking, and landscape management",
    "sweat lodge": "Ceremonial purification and prayer",
    "basket": "Used for storage, ceremony, storytelling, and trade",
    "sage": "Used for cleansing, smudging, and healing rituals"
}

def link_context(text):
    links = {}
    for key in context_map:
        if re.search(rf"\b{key}\b", text.lower()):
            links[key] = context_map[key]
    return links or {"None": "No culturally linked terms found."}

# Example use
if __name__ == '__main__':
    sample = "The elders gathered acorns and lit the fire beside the sweat lodge."
    for item, explanation in link_context(sample).items():
        print(f"🔗 {item}: {explanation}")