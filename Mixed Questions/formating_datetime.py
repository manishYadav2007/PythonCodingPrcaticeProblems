from datetime import datetime


dt_input = input("Enter the Date: ")

date_str = "%b %d %Y %I:%M%p"

date = datetime.strptime(dt_input, date_str)
print(date)

dt_format = datetime.strftime(date, "%d/%m/%Y %H:%M:%S")
print(dt_format)

