class Product:
    def __init__(self, name, price):
        self.name = name 
        self.price = price 
    
    def display_product_details(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")
        
    
    def set_expiry(self, expiry_date):
        self.expiry_date = expiry_date 
    
    def get_expiry_date(self):
        return self.expiry_date


class ElectronicsItems(Product):
    def set_warranty(self, warranty):
         self.warranty = warranty
    
    def get_warranty(self):
        return self.warranty


electronicsItemsObj  = ElectronicsItems("Motorola G53", 15000)
# electronicsItemsObj.get_warranty()
electronicsItemsObj.set_expiry("10 days")
print(electronicsItemsObj.get_expiry_date())

