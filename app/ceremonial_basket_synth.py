# CeremonialBasketSynth – Generate Basket Pattern Sequences by Function, Clan, and Totem

import random

# Motif categories by ceremonial purpose
motif_catalog = {
    "healing": ["tcwal mila", "waxpoo", "vutsierau"],
    "protection": ["venii-gemaa", "qaxkwilee", "tata'ktak"],
    "journey": ["vAnaanak", "okwEgetsip", "apxanko'ikoi"],
    "abundance": ["tcwal mila", "venii-gemaa", "xurip"],
    "vision": ["waxpoo", "qaxkwilee", "sharp-tooth"]
}

# Clan to dominant motifs
clan_emphasis = {
    "Bear": ["tcwal mila", "tata'ktak"],
    "Sturgeon": ["qaxkwilee"],
    "Snake": ["vAnaanak"],
    "Frog": ["waxpoo"],
    "Eagle": ["venii-gemaa", "okwEgetsip"]
}

def synthesize_basket(ritual, clan, length=5):
    base = motif_catalog.get(ritual.lower(), [])
    accent = clan_emphasis.get(clan.title(), [])
    full_set = base + accent
    if not full_set:
        return f"Unknown ritual '{ritual}' or clan '{clan}'"
    return random.choices(full_set, k=length)

# Example use
if __name__ == '__main__':
    basket = synthesize_basket("healing", "bear", 6)
    print("Ceremonial Basket Motif Sequence:")
    print(" → ".join(basket))
