



n = int(input("Enter the rows: "))

for i in range(1, n + 1):
    stars = "* " * i 
    spaces = " " * (n - i)
    rows = spaces + stars 
    print(rows)
for i in range(1, n ):
    stars = "* " * (n - i) 
    spaces = " " *  i 
    rows = spaces + stars 
    print(rows)
    
    
    
    

