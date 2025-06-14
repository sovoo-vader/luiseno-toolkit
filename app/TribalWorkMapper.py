# TribalWorkMapper – Suggest Tasks by Energy + Bioregion Matching

def recommend_task(season, terrain, body_state):
    map = {
        ("summer", "desert", "agile"): "Long-distance scout or herbal run",
        ("winter", "mountain", "resilient"): "Wood carrier, fire keeper",
        ("fall", "forest", "focused"): "Seed sorting or storykeeper training",
        ("spring", "valley", "rested"): "Basketmaking or ritual singing"
    }
    return map.get((season, terrain, body_state), "Camp watcher or shadow role")

if __name__ == '__main__':
    print(f"🔍 Task Suggestion: {recommend_task('fall', 'forest', 'focused')}")
