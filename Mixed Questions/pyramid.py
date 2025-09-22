n = int(input("Enter the n value: "))

for i in range(n):
    spaces = "  " * ( n - i - 1 )
    stars = "* " * ((2 * i) + 1)
    rows = spaces + stars
    print(rows) 
    
     