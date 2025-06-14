# PatternOntologyExplorer – Browse and Translate Tribal Motif Semantics

import json

# Sample ontology with cross-tribal equivalence and symbolic meaning
motif_ontology = {
    "venii-gemaa": {
        "tribes": ["Yurok", "Karok", "Hupa"],
        "meaning": "flint, tool, spark", 
        "form": "parallelogram",
        "related": ["sharp tooth", "sturgeon-back"]
    },
    "qaxkwilee": {
        "tribes": ["Yurok"],
        "meaning": "sturgeon-back, armor, flow",
        "form": "zigzag parallelograms",
        "related": ["flint", "snake"]
    },
    "waxpoo": {
        "tribes": ["Yurok"],
        "meaning": "centeredness, symmetry",
        "form": "bisected trapezoid",
        "related": ["sitting", "middle"]
    },
    "tata'ktak": {
        "tribes": ["Karok"],
        "meaning": "sharp edge, threat",
        "form": "multiple acute triangles",
        "related": ["sharp tooth", "zigzag"]
    },
    "tcwal mila": {
        "tribes": ["Hupa"],
        "meaning": "frog hand, stability, grounding",
        "form": "four triangles on vertical stalks",
        "related": ["spread hand", "foot"]
    }
}

def explore_motif(term):
    key = term.strip().lower()
    found = [k for k in motif_ontology if key in k or key in motif_ontology[k]['meaning']]
    if not found:
        return f"No matching motifs for '{term}'"
    return json.dumps({k: motif_ontology[k] for k in found}, indent=2)

# Example use
if __name__ == '__main__':
    queries = ["flint", "frog", "centered", "sharp"]
    for q in queries:
        print(f"\nMotifs related to '{q}':")
        print(explore_motif(q))
