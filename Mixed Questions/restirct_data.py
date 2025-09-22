class Mobile:
    def __init__(self, model, price, brand, secret_key):
        self.model = model 
        self.__price = price 
        self.brand = brand 
        self.__secret_key = secret_key
    
    def __show_specifications(self):
        print(f"Model: {self.model}")
        print(f"Price: {self.__price}")
        print(f"Brand: {self.brand}")    
    


    def check_price(self,  provided_secret_key):
        if self.__secret_key == provided_secret_key:
            self.__show_specifications() 
        else:
            print("Invalid Secret key!")

    def get_price(self):
        return self.__price
    
    def set_price(self, price, provided_secret_key):
        if self.__secret_key == provided_secret_key:
            self.__price = price 
        else:
            print("Invalid Secret key!")

obj = Mobile("Samsung A50s", 20000, "Samsung", "8294")



print(f"Price: {obj.get_price()}")
obj.set_price(25000, "8294")
obj.check_price("8294")









