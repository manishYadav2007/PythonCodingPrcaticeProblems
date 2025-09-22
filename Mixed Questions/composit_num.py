n = int(input("Enter the n value: "))

count =  0 

flag = False


for i in range(1, n + 1):
    if n % i == 0:
        count += 1 
        
if count > 2:
    flag = True 
else:
    flag = False 

print(flag)

        
