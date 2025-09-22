n = int(input("Enter the n value: "))

flag = 0 

for num in range(2, n):
    if n % num  == 0:
        flag += 1 
        
if flag == 0:
    print("prime Number")
else:
    print("Not a prime number")