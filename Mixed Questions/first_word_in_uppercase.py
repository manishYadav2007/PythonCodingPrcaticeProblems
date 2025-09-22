s = input("Enter the string: ")

first_word = 0 

for char in s:
    if char == " ":
        break 
    else:
        first_word += 1 

word  = s[:first_word]

upper_case = word.upper() 

new_sentence = upper_case + s[first_word:]
print(new_sentence)
