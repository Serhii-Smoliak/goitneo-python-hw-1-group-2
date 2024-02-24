from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        birthday_weekday = (today + timedelta(days=delta_days)).strftime('%A')

        if delta_days > 0 and delta_days < 7 and (birthday_weekday == 'Saturday' or birthday_weekday == 'Sunday'):
            birthday_weekday = 'Monday'

        if delta_days >= 0 and delta_days < 7:
            birthdays_per_week[birthday_weekday].append(name)

    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")

users = [
    {"name": "Bill", "birthday": datetime(1955, 12, 18)},
    {"name": "Jan", "birthday": datetime(1976, 3, 28)},
    {"name": "Kim", "birthday": datetime(1980, 1, 21)},
    {"name": "Jill", "birthday": datetime(1974, 2, 28)},
    {"name": "Pit", "birthday": datetime(1980, 2, 29)}
]

get_birthdays_per_week(users)
