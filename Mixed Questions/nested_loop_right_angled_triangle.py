n = int(input("Enter the rows value: "))


for row in range(1, n  + 1):
    for col in range(row):
        print(col + 1, end=" ")
    print()
    
    
        