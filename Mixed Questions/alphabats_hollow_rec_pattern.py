num_of_rows = int(input("Enter the value of rows: "))
num_of_col = int(input("Enter the value of columns: "))

chr_value  = chr(65)

for row in range(1, num_of_rows + 1):
    for col in range(1, num_of_col + 1):
        if row == 1 or row == num_of_rows or col == 1 or col == num_of_col:
            print(chr_value, end=" ")
        else:
            print(" ", end=" ")
        chr_value = chr(ord(chr_value) + 1)
    print() 
    
     