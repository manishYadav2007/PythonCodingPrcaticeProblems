# The code you provided is a Python script that seems to be attempting to determine the type of input
# entered by a user. However, there are some issues in the code that need to be addressed:
user_entered_value = input("Enter the user input: ")

result = ""





if int(user_entered_value.isdigit()):
    result = "Digit"

elif user_entered_value.isupper():
    result = "Uppercase Letter"

elif user_entered_value.islower():
    result = "Lowercase letter"

else:
    result = "Special Characters"
    
print(result)
 
 

