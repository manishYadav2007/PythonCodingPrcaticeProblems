n = int(input("Enter the digit: "))

sum_of_n = 0 
value_pair = 0

for i in range(n):
    value_pair = value_pair * 10 + 2 
    sum_of_n = sum_of_n + value_pair
    
    print(sum_of_n)

    


