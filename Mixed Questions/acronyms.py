string = input("Enter the string: ").split()

result = ""

for word in string:
    first_letter = word[0]
    result += first_letter
print(".".join(result))
