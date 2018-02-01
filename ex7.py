import datetime

today = datetime.datetime.now()
day = datetime.date(today.year + 1, 1, 1)

daysOfTheWeek = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

s = 0

while day.year <= today.year + 10:
    day += datetime.timedelta(days = 1)
    if day.day == today.day and day.weekday() == today.weekday():
        s += 1

print "\nIn the next 10 years,", str(s), daysOfTheWeek[today.weekday()] + "s are the " + str(today.day), "of the month they belong to!"
