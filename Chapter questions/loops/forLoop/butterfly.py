


n = 4 


for i in range(1, n + 1):
    stars = "* " * i 
    spaces = " " * 4 *( n - i)
    rows = stars + spaces + stars 
    print(rows)

for i in range(1, n):
    stars = "* " * (n - i) 
    spaces = "  " * (2 * i)
    rows = stars + spaces + stars 
    print(rows)