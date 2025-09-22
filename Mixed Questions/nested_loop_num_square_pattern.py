n = int(input("Enter the n value: "))


for row in range( n ):
    for col in range(n):
        print(col + 1, end=" ")
    print()