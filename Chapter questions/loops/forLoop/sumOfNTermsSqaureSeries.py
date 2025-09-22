
x = int(input("Enter the x term value: "))
n = int(input("Enter the nth value: "))

sum_result =  0 
value = 0 

for i in range(1, n + 1):
    value = value * 10 + x
    square = value ** 2
    sum_result +=  square
print(sum_result)


 