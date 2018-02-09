import datetime

month = int(raw_input("\nMonth: "))
while month not in range(1,13):
    print "Month must be a number from 1 to 12!"
    month = int(raw_input("\nMonth: "))

year = int(raw_input("Year: "))

months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"} 

day = datetime.date(year, month, 1)

print "\n\t\t    ", months[month], year, "\n\n\nS\tM\tT\tW\tT\tF\tS\n" + 51 * "_"

while day.month == month:
    print day.day, "\t",
    if day.weekday() == 5:
            print "\n"
    day += datetime.timedelta(days = 1)

print "\n"
