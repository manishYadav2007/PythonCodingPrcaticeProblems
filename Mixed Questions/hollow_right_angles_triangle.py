n = int(input("Enter the user input: "))


for row in range(1, n + 1):
    for column in range(1, row + 1):
        if row == 1 or row == n or column == 1 or column == row :
            print("*", end=" ")
        else:
            print("0", end=" ")
    print() 