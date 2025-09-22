




def  get_secret_msg(string_input):
    rl = []
    
    for each_char in string_input:
        if each_char.isalpha():
            rl.append(chr(219 - ord(each_char.lower())))
        else:
            rl.append(each_char)
    return "".join(rl)









string_input = input("Enter a string: ")

result = get_secret_msg(string_input)
print(f"Secret message: {result}")
