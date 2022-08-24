# https://www.hackerrank.com/challenges/calendar-module/problem

import datetime

month, day, year = list(map(int, input().split()))

date       = datetime.date(year, month, day)
day_number = date.weekday()

# If since Hackerrank Python version is less than 3.10
if day_number == 0:
    print("MONDAY")
elif day_number == 1:
    print("TUESDAY")
elif day_number == 2:
    print("WEDNESDAY")
elif day_number == 3:
    print("THURSDAY")
elif day_number == 4:
    print("FRIDAY")
elif day_number == 5:
    print("SATURDAY")
elif day_number == 6:
    print("SUNDAY")
