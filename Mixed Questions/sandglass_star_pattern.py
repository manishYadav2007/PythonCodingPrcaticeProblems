
n = int(input("Enter the number of rows: "))

for rows in range(n, 0, -1):
    print(" " * (n - rows), end="")
    for column in range(rows):
        print("*", end=" ")
    print()
    
for rows in range(2, n + 1 ):
    print(" " * (n - rows), end="")
    for column in range(rows):
        print("*", end=" ")
    print()
    
    