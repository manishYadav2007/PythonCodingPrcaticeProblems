string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


result = ""


for i in range(len(string1)):
    if i % 2 == 0:
        result += string1[i]
    else:
        result += string2[i]
print(result)