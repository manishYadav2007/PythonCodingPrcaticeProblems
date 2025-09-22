from datetime import datetime, timedelta


d1 = input("Entr the first date: ")
d2 = input("Entr the second date: ")

date_format = "%d %b %Y"



date_1 = datetime.strptime(d1, date_format)
date_2 = datetime.strptime(d2, date_format)

diff_days = (date_2 - date_1).days
# print(diff_days)

sat_count = 0 
sun_count = 0 

for each_day in range(diff_days + 1):
    current_days = date_1 + timedelta(days=each_day)
    weekdays = current_days.weekday()
    
    if weekdays == 5:
        sat_count += 1
    elif weekdays == 6:
        sun_count += 1 
    
print(f"Saturday:", sat_count)
print(f"Sunday:", sun_count)


