# SaintDayMapper - Link Dates and Places to Patron Saints from Missionary Calendars

import datetime

# Simplified Spanish mission saint calendar (expandable)
saint_calendar = {
    1: "San Manuel", 2: "Santa Clara", 3: "San Blas", 4: "Santa Verónica",
    5: "San Felipe", 6: "San Norberto", 7: "Santa Rosa", 8: "San Roque",
    9: "San Gorgonio", 10: "San Francisco", 11: "San Diego", 12: "Santa Lucía",
    13: "Santa Teresa", 14: "San Valentín", 15: "San Raimundo", 16: "Santa Elena",
    17: "San Patricio", 18: "San Benito", 19: "San José", 20: "San Isidro",
    21: "Santa Marta", 22: "San Luis", 23: "Santa Inés", 24: "San Gabriel",
    25: "Santa Catalina", 26: "San Antonio", 27: "Santa Bárbara", 28: "San Juan",
    29: "Santa Margarita", 30: "San Sebastián", 31: "San Ramón"
}

# Assign a saint to a date or location
def map_saint(day=None):
    today = datetime.date.today()
    if day is None:
        day = today.day
    saint = saint_calendar.get(day, "Unknown Patron")
    return f"Day {day}: {saint}"

# Example use
if __name__ == '__main__':
    for d in [1, 11, 19, 25]:
        print(map_saint(d))
