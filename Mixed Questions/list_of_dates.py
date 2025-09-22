# from datetime import datetime, timedelta


# start_date = input("Enter the string date: ")
# end_date = input("Enter the end date: ")

# start_dt_format = "%b %d %Y"
# end_dt_format = "%b %d %Y"


# date1 = datetime.strptime(start_date, start_dt_format)
# date2 = datetime.strptime(end_date, end_dt_format)


# days = (date2 - date1).days 

# for each_day in range(1, days + 1):
#     list_of_date = date1 + timedelta(days=each_day)
#     print(list_of_date)
    
    
    

















from datetime import datetime, timedelta 



start_dt = input("Enter the start date: ")
end_dt = input("Enter the end date: ")


start_dt_format  = datetime.strptime(start_dt, "%b %d %Y" )
end_dt_format = datetime.strptime(end_dt, "%b %d %Y")

print(start_dt_format)
print(end_dt_format)

days_interval = (end_dt_format - start_dt_format).days
print(days_interval)


for each_day in range(1, days_interval + 1):
    print(start_dt_format + timedelta(days=each_day))
    
    
    
























