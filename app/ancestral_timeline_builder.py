# AncestralTimelineBuilder – Extract and Sequence Generational References

import re

def extract_generational_phrases(text):
    patterns = [
        r"my (great-)?grandfather",
        r"his ancestors",
        r"the (first|last) people",
        r"our elders",
        r"children of",
        r"descendants of"
    ]
    results = []
    for pattern in patterns:
        matches = re.findall(pattern, text.lower())
        results.extend(matches)
    return sorted(set(results)) or ["None"]

# Example
if __name__ == '__main__':
    text = "My grandfather told stories of the first people. Our elders remember when the sky cracked."
    print("🧬 Generational Phrases:", extract_generational_phrases(text))