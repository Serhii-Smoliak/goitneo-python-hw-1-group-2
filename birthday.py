'''This module outputs a list of employees grouped by the days of the week
    whose birthdays fall within the next 7 days, including the day
    the function is called.'''

from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    '''Function that returns employees birthday list'''
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

        if 0 <= delta_days < 7:
            if birthday_weekday in ['Saturday', 'Sunday']:
                birthday_weekday = 'Monday'
            birthdays_per_week[birthday_weekday].append(name)

    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")
