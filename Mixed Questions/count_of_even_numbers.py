str_num = input("Enter the string: ")

count = 0 


for i in  str_num:
    
    if int(i) % 2 == 0:
        count += 1 

if count > 2:
    print("Count of even digits is greater than 2")
else:
    print("Count of even digits is not greater than 2")
    