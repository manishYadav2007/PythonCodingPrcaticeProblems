n = int(input("Enter the nth number: "))

for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i 
    row = spaces + stars
    print(row)
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    stars = "* " * i 
    row = spaces + stars
    print(row)