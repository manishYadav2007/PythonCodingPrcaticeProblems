



def pin_validation(pin):
    if pin.isdigit() and len(pin) == 4 or len(pin) == 6:
        return "Valid Pin"
    else:
        return "Invalid PIN"




pin  = input("Enter your atm pin here: " )

result = pin_validation(pin)
print(result)
