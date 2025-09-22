n = int(input("Enter the input n: "))
m  = int(input("Enter the value of m: " ))
sum_of_prime_num = 0 


for num in range(n, m + 1):
    if num > 1:
        for j in range(2, num):
            if (num % j) == 0:
                break
        else:
            sum_of_prime_num += num 
print(sum_of_prime_num)

