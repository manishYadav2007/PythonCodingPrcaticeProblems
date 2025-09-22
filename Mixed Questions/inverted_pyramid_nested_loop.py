n = int(input("Enter the value of n: "))

for row in range(n, 0, -1):
    print(" " * (n - row), end="")
    for column in range(1, row + 1):
        print(column, end=" ")
    print() 