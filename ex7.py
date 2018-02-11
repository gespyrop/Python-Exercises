import datetime

today = datetime.datetime.now()
day = datetime.date(today.year + 1, 1, 1)

daysOfTheWeek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

s = 0

while day.year <= today.year + 10:
    day += datetime.timedelta(days = 1)
    if day.day == today.day and day.weekday() == today.weekday():
        s += 1

print "\nIn the next 10 years,", str(s), daysOfTheWeek[today.weekday()] + "s are the " + str(today.day), "of the month they belong to!"
