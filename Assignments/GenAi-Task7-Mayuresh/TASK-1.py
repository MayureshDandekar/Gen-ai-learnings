class Product:
    def __init__(self, name , price, category):
        self.name = name 
        self.price = price
        self.category = category

    def get_info(self):
        return f"Product name : {self.name} | Price : {self.price} | Category : {self.category}"

    def apply_discount(self, percent):
        # discount = percent/100
        discount_price = self.price * (1-percent/100)
        return f"Price after Discount is {discount_price}"


p1 = Product("Tv", 100, "electronic")
p2 = Product("Chair", 100, "Furniture")
print(p1.get_info())
print(p2.get_info())
print(p1.apply_discount(50))
print(p2.apply_discount(5))

