x = int(input("Enter the x value: "))
n = int(input("Enter the n value: "))

sum_result = 0 
value = 0 

for i in range(1, n + 1):
    value = value * 10 + x 
    sum_result += value 
print(f"Your answer will be: {sum_result}") 

