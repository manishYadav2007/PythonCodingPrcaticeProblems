

n = int(input("Enter the target number: "))

count_number = 0 
original_number = n 


str_num = str(n)

for i in  str_num:
    digit = int(i)
        
    if digit != 0 and original_number % digit == 0:
        count_number += 1 
print(count_number)

