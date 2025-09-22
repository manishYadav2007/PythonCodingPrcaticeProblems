



n = 5 


for i in range(1, n + 1):
    if i == 1:
        row = "* " * n
    elif i == n:
        row = "* " * n
    else:
        hollow_square = "0 " * (n - 2)
        row = "* " + hollow_square + "*"
    print(row)
