# ResilienceIndexAI – Rate Personal Hardiness by Nature-Exposure Profiles

def calculate_resilience_score(cold_tolerance, rain_endurance, fasting_hours, movement_hours):
    score = 0
    score += min(cold_tolerance / 30, 1) * 25  # scale max 30 min cold
    score += min(rain_endurance / 15, 1) * 25  # max 15 min in rain
    score += min(fasting_hours / 18, 1) * 25   # max benefit assumed at 18h
    score += min(movement_hours / 5, 1) * 25   # active hrs (walking etc)
    return round(score, 1)

if __name__ == '__main__':
    result = calculate_resilience_score(cold_tolerance=20, rain_endurance=12, fasting_hours=16, movement_hours=4)
    print(f"🧬 Resilience Index: {result}/100")
