value_one = int(input("Enter the value one: " ))
value_two = int(input("Enter the value two: "))

gcd = 1 

min_value = min(value_one, value_two)
print(min_value)

for i in range(1, min_value + 1):
    if value_one % i == 0 and value_two % i == 0:
        gcd = i     
print(gcd)








