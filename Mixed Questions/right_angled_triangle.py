rows = int(input("Enter the rows: ")) # 3

for i in range(1, rows + 1):
    spaces = " " * (rows - i )
    stars = "* " * i 
    row = spaces + stars
    print(row)
    
