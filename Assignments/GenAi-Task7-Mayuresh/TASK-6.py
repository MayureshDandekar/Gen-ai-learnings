class Product:
    def __init__(self, name , price , category):
        self.name = name 
        self.__price = price 
        self.category = category

    def __str__(self):
        return f"Product({self.name}, {self.__price}, {self.category})"

    def __add__(self, other):
        return self.__price + other.__price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price>0:
            self.__price = new_price

    def get_info(self):
        return f"Product name : {self.name} | Price : {self.get_price()} | Category : {self.category}"


product1 = Product("Tv", 10000, "Electronic")
product2 = Product("Camera", 10000, "Electronic")
print(product1) 
total = product1 + product2
print(total)

