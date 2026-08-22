class Product:
    def __init__(self, name , price , category):
        self.name = name 
        self.__price = price 
        self.category = category

    def __str__(self):
        return f"Product({self.name}, {self.__price}, {self.category})"

    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price + other.__price
        return NotImplemented


    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price>0:
            self.__price = new_price

    def get_info(self):
        return f"Product name : {self.name} | Price : {self.get_price()} | Category : {self.category}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                break

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.get_price()
        return total

    def show_all_product(self):
        for product in self.products:
            print(product.get_info())

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self, product):
        self.inventory.add_product(product)

    def show_summary(self):
        print(f"Store Name: {self.store_name}")
        print(f"Total items are {len(self.inventory.products)} and total value is {self.inventory.get_total_value()}")



# Createing products
p1 = Product("Tv", 10000, "Electroni")
p2 = Product("Camera", 50000, "Electroni")
p3 = Product("Laptop", 90000, "Electroni")
p4 = Product("Mobile", 30000, "Electroni")

# Creating inventory object and adding products
inventory = Inventory()
inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

print("Products in Inventory")
for product in inventory.products:
    print(product)

print(f"Total value of products is {inventory.get_total_value()}")

inventory.remove_product("Tv")
# print("\nAfter removing Tv")
# for product in inventory.products:
#     print(product)

inventory.show_all_product()

# Creating store object and adding products with summary
store = Store("My Store")
store.add_new_product(p1)
store.add_new_product(p2)
store.add_new_product(p3)
store.add_new_product(p4)
store.show_summary()


# combining two products
total_price = p1 + p2
print(f"Total price of {p1.name} and {p2.name} is {total_price}")