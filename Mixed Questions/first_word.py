string = input("Enter the string value: ")


count =  0 

for c in string:
    if c == " ":
        break
    else:
        count += 1

first_word = string[:count]
print(first_word)

