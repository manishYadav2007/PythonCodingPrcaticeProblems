password = input("Enter the password: ")

digit = 0

for i in password:
    is_digit = i.isdigit()
    
    if is_digit:
        digit += 1 
if digit > 0:
    print("Valid Password") 
else:
    print("Invalid Password")
    
    

