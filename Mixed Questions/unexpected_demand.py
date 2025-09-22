def filledOrders(order, k):
    # Order list ko sort kar lete hain
    order.sort()
    
    total_widgets_used = 0
    fulfilled_orders = 0
    
    # Order ke har item ke liye loop chalaate hain
    for widgets_needed in order:
        if total_widgets_used + widgets_needed <= k:
            total_widgets_used += widgets_needed
            fulfilled_orders += 1
        else:
            break
    
    return fulfilled_orders

# User se total number of orders input lete hain
num_of_orders = int(input("Enter the number of orders: "))

orders_list = []

# Har order size ke liye input lete hain
for each_order in range(1, num_of_orders + 1):
    orders = list(map(int, input("Enter the order sizes separated by space: ").split()))
    orders_list.append(orders)  # Corrected line

# Number of widgets ki input
widgets = int(input("Enter the number of widgets: "))

# Ab har ek order list ke liye filledOrders function call karte hain
for index, order in enumerate(orders_list, start=1):
    result = filledOrders(order, widgets)
    print(f"Order {index}: Fulfilled {result} orders.")