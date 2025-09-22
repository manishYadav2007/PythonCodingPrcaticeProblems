import datetime


year = int(input("Enter the year: "))
months = int(input("Enter the Month: "))
days = int(input("Enter the days: "))

date = datetime.date(year, months, days)
print(date)

