n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    
    stars = "* " * i 
    spaces = " " * 4 * (n - i)
    rows = stars + spaces + stars
    print(rows) 
    
    
    
    