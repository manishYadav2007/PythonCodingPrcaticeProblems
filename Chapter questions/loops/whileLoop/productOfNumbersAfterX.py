
n = int(input("Enter the target value: "))
# 4 
range_value = int(input("Enter the range value: "))
# 2


p =  1 
i = 1 

while i <= range_value: # 1 <= 4
    p *= (n + i)
    i += 1 
print(p)
    