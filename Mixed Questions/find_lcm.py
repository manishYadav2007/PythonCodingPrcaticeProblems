# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))

# max_num = max(a, b)

# range_value = a * b 


# for num in range(max_num, range_value + 1):
#     if num % a ==  0 and num % b == 0:
#         lcm = num 
#         break 
# print(lcm)



# This Python code is calculating the Least Common Multiple (LCM) of two numbers entered by the user.

a = int((input("Enter your first value: ")))
b = int((input("Enter your second value: ")))


max_value = max(a , b)
range_value = a * b 

for i in range(max_value, range_value + 1):
    if i % a == 0 and i % b == 0:
        lcm  = i
        break
    
print(lcm)
