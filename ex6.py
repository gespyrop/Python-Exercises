import datetime

month = int(raw_input("\nMonth: "))
while month not in range(1,13):
    print "Month must be a number from 1 to 12!"
    month = int(raw_input("\nMonth: "))

year = int(raw_input("Year: "))
