

m = int(input("Enter the start number: "))
n = int(input("Enter the end number: "))

count  = 0

for i in range(m, n + 1):
    if i < 10:
        count += 1
    elif i  < 100:
        count += 2 
    elif i < 1000:
        count += 3 
    elif i < 10000:
        count += 4 
    else:
        count += len(str(i))

print(count)
        


