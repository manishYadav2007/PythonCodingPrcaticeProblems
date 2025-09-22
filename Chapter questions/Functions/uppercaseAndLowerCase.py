



def get_uppercase_and_lowercase(string_input):
    uppercase = ""
    lowercase = ""
    for char in string_input:
        if char.isupper():
            uppercase += char 
        else:
            lowercase += char 
    print(uppercase)
    print(lowercase)
    



string_input  = input("Enter the string input: ")

get_uppercase_and_lowercase(string_input)

