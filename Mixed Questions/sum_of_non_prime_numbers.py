def get_sum_of_non_prime_numbers(num_of_inputs):
    sum_of_prime_numbers = []
    
    for i in range(1, num_of_inputs + 1):
        num = int(input("Enter the value: "))
        if num > 1:
            for j in  range(2, num):
                if num % j == 0:
                    sum_of_prime_numbers.append(num)
                    print(sum(sum_of_prime_numbers))
                    break
                
                

num_of_inputs = int(input("Enter the number of inputs: "))


get_sum_of_non_prime_numbers(num_of_inputs)