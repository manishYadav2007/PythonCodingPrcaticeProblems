class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price 
        self.deal_price = deal_price
        self.ratings = ratings 
        self.you_save = price - deal_price
    
    def display_product_details(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")
        print(f"Product Deal Price: {self.deal_price}")
        print(f"Product Ratings: {self.ratings}")
        print(f"Customer Saved: {self.you_save}")    
    
    def get_deal_price(self):
        return self.deal_price


class ElectronicsItem(Product):
    
    def __init__(self, name, price, deal_price, ratings, warranty_in_months):
        super().__init__ (name, price, deal_price, ratings)
        self.warranty_in_months = warranty_in_months
    
    
    def display_product_details(self):
        super().display_product_details()
        print(f"warranty: {self.warranty_in_months} months")


class GrocerryItems(Product):
    
    def __init__(self,  name, price, deal_price, ratings, expiry_date):
        super().__init__(name, price, deal_price, ratings)
        self.expiry_date = expiry_date 
        
    def display_product_details(self):
        super().display_product_details()
        print(f"Expiry Date: {self.expiry_date}")
        


class Order:
    def __init__(self,  delivery_address, payment_method):
        self.delivery_address = delivery_address
        self.payment_method = payment_method
        self.items_in_cart  = []
    
    
    def add_items(self,  product, quantity):
        self.items_in_cart.append((product, quantity))
    
    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print(f"Product: {product.name},  Quantity: {quantity}")
            print("")
    
    def get_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price 
        print(f"Total Bill: {total_bill}")
        return total_bill
    



obj1 = ElectronicsItem("Iphone 12", 100000, 90000, 4.5, 12)
obj2 = GrocerryItems("Milk", 20, 30, 4.2, 12)
obj2.display_product_details()
print("")
obj1.display_product_details()
print("")

orderObj = Order("Bokaro", "UPI"); 
orderObj.add_items(obj1, 2)
orderObj.add_items(obj2, 5)
orderObj.display_order_details()
orderObj.get_total_bill()








