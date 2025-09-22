

def get_trades(list_of_customers):
    total_trade = 5 / 100 * len(list_of_customers)
    print(total_trade)
    count_each_customer = {}
    
  # This part of the code is iterating through the list of customers and counting the occurrences of
  # each customer in the list.
    for i in list_of_customers:
       # This part of the code is checking if the current customer `i` is already present in the
       # `count_each_customer` dictionary. If the customer `i` is already a key in the dictionary, it
       # increments the count of that customer by 1. If the customer `i` is not already in the
       # dictionary, it adds the customer as a key with a count of 1.
        if i in count_each_customer:
            count_each_customer[i] += 1 
        else:
            count_each_customer[i] = 1
    
    active_customers = []
    
    for customer, count in count_each_customer.items():
        
        if count >= total_trade:
            active_customers.append(customer)
    active_customers.sort()

    return active_customers
        
        

list_of_customers = input("Enter the customer: ").split()
result = get_trades(list_of_customers)
print(result)





