# OutdoorSleepProtocol – Advisor for Natural Circadian Restoration
import datetime

ideal_conditions = {
    "temp_range_c": (7, 18),
    "humidity_range": (20, 60),
    "moonlight": False,
    "quiet_hours": (21, 5)
}

def assess_conditions(temp_c, humidity_pct, moon_visible, current_hour):
    score = 0
    if ideal_conditions["temp_range_c"][0] <= temp_c <= ideal_conditions["temp_range_c"][1]:
        score += 1
    if ideal_conditions["humidity_range"][0] <= humidity_pct <= ideal_conditions["humidity_range"][1]:
        score += 1
    if not moon_visible:
        score += 1
    if current_hour in list(range(ideal_conditions['quiet_hours'][0], 24)) + list(range(0, ideal_conditions['quiet_hours'][1])):
        score += 1

    return f"🌒 Outdoor Sleep Score: {score}/4 — {'Recommended' if score >= 3 else 'Not Ideal'}"

if __name__ == '__main__':
    now = datetime.datetime.now()
    print(assess_conditions(temp_c=14, humidity_pct=45, moon_visible=False, current_hour=now.hour))
