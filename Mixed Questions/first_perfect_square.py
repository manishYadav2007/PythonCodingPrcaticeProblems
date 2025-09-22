# m = int(input("Enter the value of m: "))
# n = int(input("Enter the value of n: "))


# found = False

# for i in range(m, n + 1):
#     for j in range(1, i + 1):
#         if j * j == i:
#             print(i)
#             found = True
#     if found:
#         break
# if not found:
#     print("No Perfect Square")




















m = int(input("Enter your first number: "))
n = int(input("Enter your second number: "))

found = False 

for num in range(m, n + 1):
    for i in range(1, num + 1):
        if i * i == num:
            print(num)
            found = True
    if found:
        break 
if not found:
    print("No Perfect Square") 







