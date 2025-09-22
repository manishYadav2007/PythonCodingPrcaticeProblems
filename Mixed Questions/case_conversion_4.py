string = input("Enter the string: ")


result = ""


for char in string:
    if char.isupper():
        char = char.lower()
        result = result + "_" + char
    else:
        result += char 
print(result.strip("_"))