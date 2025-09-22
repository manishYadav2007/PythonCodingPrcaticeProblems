start_num = int(input("Enter the start value: "))
end_num = int(input("Enter the end value: "))


count = 0 


for num in range(start_num, end_num + 1):
    if num > 1:
        for j in range(2, num):
            if (num % j == 0):
                print(num)
                count += 1 
                break
            
            

