class Product:
    def __init__(self, name , price , category):
        self.name = name 
        self.__price = price 
        self.category = category

    def get_info(self):
        return f"Product name : {self.name} | Price : {self.get_price()} | Category : {self.category}"

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price>0:
            self.__price = new_price


class Laptop(Product):
    def __init__(self, name, price, category):
        super().__init__(name, price, category)

    def get_info(self):
        return "Laptop-->\n" + super().get_info() 


class Mobile(Product):
    def __init__(self, name, price, category):
        super().__init__(name, price, category)

    def get_info(self):
        return "Mobile-->\n" + super().get_info()


p1 = Laptop("Laptop", 100000, "Electronic")
p2 = Mobile("Mobile", 10000, "Electronic")
products = [p1,p2]

for product in products:
    print(product.get_info() )