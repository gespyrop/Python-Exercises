import datetime

today = datetime.datetime.now()
day = today

Monday8 = 0

while day.year <= today.year + 10:
    if day.day == 8 and day.weekday() == 0:
        Monday8 += 1
    day += datetime.timedelta(days = 1)

print "\nIn the next 10 years,%d Mondays are the 8th of the month they belong to!" % Monday8
