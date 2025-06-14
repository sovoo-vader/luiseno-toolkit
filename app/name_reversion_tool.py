# NameReversionTool - Reconstruct Original Indigenous Roots from Corrupted Spanish Names

import difflib

# Sample mapping: corruptions of Indigenous words into Spanish
phonetic_registry = {
    "La Jolla": ["La Hoya", "La Joya", "Lahoya", "Hoyak", "Juhuya"],
    "Temecula": ["Temeku", "Tumecku", "Tameka", "Temekuyam"],
    "Tia Juana": ["Tiwana", "Tiawana", "Taywanak", "Tiuwanak"]
}

# Reference sound bank (Indigenous-derived syllables / roots)
indigenous_syllables = ["tem", "eku", "jo", "ya", "pala", "ama", "ish", "towa", "kuya"]

def revert_name(modern_name):
    if modern_name not in phonetic_registry:
        return f"No known reversion path for '{modern_name}'"
    variants = phonetic_registry[modern_name]
    best_match = difflib.get_close_matches(modern_name.lower(), variants, n=1)
    if best_match:
        return f"'{modern_name}' likely derives from indigenous root: '{best_match[0]}'"
    return f"Indigenous root of '{modern_name}' is ambiguous."

# Example use
if __name__ == '__main__':
    samples = ["La Jolla", "Temecula", "Tia Juana", "Cuyamaca"]
    for name in samples:
        print(revert_name(name))
