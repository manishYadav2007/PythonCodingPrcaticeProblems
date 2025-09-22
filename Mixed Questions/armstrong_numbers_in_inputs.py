n = int(input("Enter the value of n: "))

armstrong_num = []

for _ in range(n):
    num = int(input("Enter the number: "))
    str_num = str(num)
    len_of_num = len(str_num)
    sum_of_armstrong_num = 0
    for digit in str_num:
        sum_of_armstrong_num += int(digit) ** len_of_num
    if sum_of_armstrong_num == num:
        armstrong_num.append(num)
        print(armstrong_num)


for each_num in armstrong_num:
    print(each_num)
        
    