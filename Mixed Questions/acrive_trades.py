
# Define a function to get the list of active customers
def  get_trades(list_of_customers):
    # Calculate the total number of trades
    total_trades = 5 / 100 * len(list_of_customers)
    # Create an empty dictionary to store the count of each customer
    count_each_customer = {}
    # Loop through the list of customers
    for i in list_of_customers:
        # If the customer is already in the dictionary, increment the count
        if i in count_each_customer:
            count_each_customer[i] += 1
        # If the customer is not in the dictionary, add them with a count of 1
        else:
            count_each_customer[i] = 1 
    
    # Create an empty list to store the active customers
    active_customers = []
    
    # Loop through the dictionary of customers and their counts
    for customer, count in count_each_customer.items():
        # If the count is greater than or equal to the total number of trades, add the customer to the list
        if count >= total_trades:
            active_customers.append(customer)
    
    # Sort the list of active customers
    active_customers.sort()
    
    # Return the list of active customers
    return active_customers




# Get the list of customers from user input
list_of_customers = input("Enter the customers: ").split()


# Call the function to get the list of active customers
result = get_trades(list_of_customers)
# Print the list of active customers
print(result)