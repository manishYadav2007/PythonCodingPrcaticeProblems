def calculate_bill(amount):
    # Complete this function
    discount_result = None 
    if amount < 500:
        discount_result = ((5 /100) * amount) 
        return  amount - discount_result 
    elif amount >= 500 and amount <= 2500:
        discount_result = (10 / 100) * amount 
        return amount - discount_result 
    elif amount >= 2500:
        discount_result = (20 / 100) * amount 
        return amount - discount_result 

amount = int(input("Enter the bill amount: "))
# Call the calculate_bill function
print(calculate_bill(amount))
