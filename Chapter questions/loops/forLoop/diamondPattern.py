

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    spaces =  n - i
    stars =  i 
    row = (" ") * spaces + ("* ")* stars 
    print(row)    
for i in range(1 , n):
    spaces =  i 
    stars =  n - i
    row = (" ") * spaces + ("* ")* stars 
    print(row)    




     
    