n = input("Enter the number: ")

len_of_number = len(n)

sum_counter = 0

for i in n:
    sum_counter   += int(i) ** len_of_number

if  sum_counter == int(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number") 





    
