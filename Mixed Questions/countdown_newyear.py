from datetime import datetime


dt_input = input("Enter the date: ")

dt_str = "%b %d %Y %I:%M %p" # format of input date 

date = datetime.strptime(dt_input, dt_str) 

new_year = datetime(date.year + 1, 1, 1, 0, 0) # increase year + 1, day, month, hour, minute


diff = new_year - date 
print(diff)


total_minutes = (int(diff.total_seconds()) // 60) 
print(total_minutes)

hours = total_minutes // 60 
print(hours)

minutes = total_minutes % 60 
print(minutes)




print(f"{hours} Hours {minutes} Minutes")




