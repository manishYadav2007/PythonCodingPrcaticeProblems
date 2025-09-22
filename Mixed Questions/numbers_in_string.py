n = input("Enter the value of n: ")

count_of_n = 0
sum_of_n = 0


for i in n:
    if i.isdigit():
        sum_of_n += int(i)
        count_of_n += 1 

if count_of_n > 0:
    avg = sum_of_n / count_of_n
    rounded_avg_value = round(avg, 2)
    
    print(sum_of_n)
    print(rounded_avg_value)
