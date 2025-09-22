n = int(input("Enter the rows: "))
m = int(input("Enter the columns: "))


for row in range(n):
   for columns in range(m):
       if row == 0 or row == n - 1 or columns == 0 or columns == m - 1:
           print("*", end=" ")
       else:
           print("0", end=" ")
   print() 
        


    
    