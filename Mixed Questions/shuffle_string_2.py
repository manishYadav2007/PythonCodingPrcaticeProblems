string  = input("Enter the string: ")

length = len(string)


result = ""


for i in range(length):
    index = int(input("Enter the index: "))
    
    result += string[index]
print(result)



