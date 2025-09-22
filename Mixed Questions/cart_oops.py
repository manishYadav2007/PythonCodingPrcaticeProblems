class Cart:
    
    def __init__(self):
        self.items = {}
        self.price_details = {
            "Shoe": 1350,
            "Keyboard": 950,
            "Monitor": 3550,
            "Laptop": 55000
        } 
    
    def add_items(self, item_name, quantity):
        self.items[item_name] = quantity
    
    def get_cart_items(self):
        return list(self.items.keys()) 
    
    def remove_items(self, item_name):
        del self.items[item_name] 
    
    def update_items(self, item_name, quantity):
        self.items[item_name] = quantity 
    
    def get_total_price(self):
        total_price = 0 
        for items, quantity in self.items.items():
            total_price += quantity * self.price_details[items]
        return total_price 
       


cartItems = Cart()
cartItems.add_items("Shoe", 10)
cartItems.add_items("Keyboard", 15)
cartItems.add_items("Monitor", 5)
cartItems.add_items("Laptop", 6)
print(cartItems.items)
print("")
cartItems.remove_items("Shoe")
print(cartItems.items)
cartItems.update_items("Monitor", 30)
print(cartItems.items)
print(cartItems.get_total_price())







