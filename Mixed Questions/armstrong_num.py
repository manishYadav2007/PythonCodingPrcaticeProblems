

n = int(input("Enter the starting value: "))
m = int(input("Enter the end value: "))
armstrong_num = []

for i in range(n, m + 1):
    str_num = str(i)
    len_of_num = len(str_num)
    armstrong_sum = 0 
    for j in str_num:
        armstrong_sum = armstrong_sum + int(j) ** len_of_num
    if armstrong_sum == i:
        armstrong_num.append(armstrong_sum)
        
if armstrong_num:
    print(" ".join(map(str, armstrong_num)))
else:
    print(-1)
    
    


    
    
    