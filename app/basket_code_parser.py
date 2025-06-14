# BasketCodeParser – Decodes Basket Imagery into Named Design Motifs

import re
from difflib import get_close_matches

# A simplified symbolic lexicon from Yurok-Karok-Hupa vocab
known_motifs = {
    "venii-gemaa": "flint/parallelogram",
    "veniirpeLaa": "sharp-tooth/acute triangle",
    "qaxkwilee": "sturgeon-back (zigzag parallelograms)",
    "okwEgetsip": "spread hand (paired vertical angles)",
    "vutsierau": "ring/encircling band",
    "waxpoo": "centered trapezoid with triangle",
    "tcwal mila": "frog hand (four triangles on stalks)",
    "vAnaanak": "diagonal stripe (motion/spotted)",
    "xurip": "striped (vertical bars)",
    "apxanko'ikoi": "progressive trapezoids (up/down motion)"
}

# Simulated visual element input (normally from CV model)
sample_elements = ["parallelogram", "acute triangle", "zigzag parallelograms",
                   "four upward angles", "diagonal stripes", "ring band"]

def parse_elements_to_motifs(elements):
    results = {}
    for el in elements:
        closest = get_close_matches(el, known_motifs.values(), n=1, cutoff=0.6)
        if closest:
            match = [k for k, v in known_motifs.items() if v == closest[0]][0]
            results[el] = match
        else:
            results[el] = "Unrecognized motif"
    return results

# Example usage
if __name__ == '__main__':
    motifs = parse_elements_to_motifs(sample_elements)
    for pattern, code in motifs.items():
        print(f"'{pattern}' → {code}")
