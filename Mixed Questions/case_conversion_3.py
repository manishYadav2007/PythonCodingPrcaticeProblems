string = input("Enter the string: ")

result  = ""

for i in string:
    if i.isupper():
        i = i.lower()
        
        result += "-" + i 
    else:
        result = result + i 



print(result.lstrip("-"))