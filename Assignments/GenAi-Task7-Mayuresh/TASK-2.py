class Product:
    def __init__(self, name , price , category):
        self.name = name 
        self.__price = price 
        self.category = category

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price>0:
            self.__price = new_price 

p1 = Product("Tv", 1000, "Electronic")
print(p1.get_price()) 
p1.set_price(10000)
print(p1.get_price()) 

        