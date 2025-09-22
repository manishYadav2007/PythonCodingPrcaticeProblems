import datetime

reference_date = datetime.datetime(1970, 1, 1)

seconds_input = int(input("Enter the seconds: "))

seconds_object = datetime.timedelta(seconds=seconds_input)

result_date = reference_date + seconds_object
print(result_date)

dt_format = "%Y-%m-%d %H:%M:%S"

new_dt = result_date.strftime(dt_format)
print(new_dt)

