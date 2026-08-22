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

class ElectronicProduct(Product):
    def __init__(self, name , price , category, warranty_year):
        super().__init__(name, price, category)
        self.warranty_year = warranty_year
    def get_info(self):
        return super().get_info() +  f"| Warranty : {self.warranty_year} Years"




p2 = ElectronicProduct("Camera", 10000, "Electronic", 7)
print(p2.get_price())
print(p2.get_info())
        