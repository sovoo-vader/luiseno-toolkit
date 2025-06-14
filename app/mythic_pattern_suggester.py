# MythicPatternSuggester – Generate Basket Pattern Archetypes by Theme and Story Use

pattern_map = {
    ("journey", "night"): "qaxkwilee – zigzag sturgeon-back for directionless flow",
    ("healing", "grief"): "tcwal mila – frog hand for emotional anchoring",
    ("protection", "childbirth"): "vutsierau – enclosing ring for sacred boundaries",
    ("memory", "ancestor"): "waxpoo – centered trapezoid for lineage mark",
    ("vision", "mountain"): "apxanko'ikoi – ascending trapezoids for elevated clarity"
}

def suggest_pattern(purpose, theme):
    key = (purpose.lower(), theme.lower())
    return pattern_map.get(key, "🌀 No known pattern for this combination")

# Example use
if __name__ == '__main__':
    result = suggest_pattern("healing", "grief")
    print(f"🔮 Suggested Pattern: {result}")
