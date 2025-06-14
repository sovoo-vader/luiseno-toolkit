# NamedEntityExtractor – Identify Mythic Figures and Deities from Luiseño Corpus

import re

# Sample corpus and mythology names
myth_figures = ["Túpanax", "Núkat", "Wiot", "Weywot", "Toómal"]

def extract_named_entities(text):
    found = []
    for name in myth_figures:
        if re.search(rf"\b{name}\b", text):
            found.append(name)
    return found or ["None"]

# Example
if __name__ == '__main__':
    sample_text = "Núkat and Túpanax met at the red canyon before Wiot vanished."
    print("🧙 Named Entities:", extract_named_entities(sample_text))