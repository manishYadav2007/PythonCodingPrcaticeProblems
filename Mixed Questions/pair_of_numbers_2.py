n = int(input("Enter the value of n: "))

count  = 0

for i in range(1, (n // 2) + 1):
    b = n - i 
    if i < b:
        count += 1 
print(count) 