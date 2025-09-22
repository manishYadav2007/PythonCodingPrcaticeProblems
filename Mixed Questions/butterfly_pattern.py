n = int(input("Enter the nth number: "))


for row in range(1, n + 1):
    stars = "* " * row 
    spaces = " " * 4 * (n - row)
    rows = stars + spaces + stars
    print(rows)

for row in range(n - 1, 0, -1 ):
    stars = "* " * row 
    spaces = " " * 4 * (n - row)
    rows = stars + spaces + stars
    print(rows)
    
    
    
    
    
    
    
    