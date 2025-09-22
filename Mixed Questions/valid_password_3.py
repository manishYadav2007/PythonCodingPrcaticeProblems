password = input("Enter the password: ")

is_digit_contain = False

for i in password:
    is_digit = i.isdigit()
    if is_digit:
        is_digit_contain = True 

is_upper = password.upper == password
is_lower = password.lower == password

is_upper_and_lower = (not is_upper) and (not is_lower)


is_password_valid = is_upper_and_lower and is_digit_contain


if is_password_valid:
    print("Valid Password")
else:
    print("Invalid Password")



