# class Book:

#     def __init__(self, book, pages):
#         self.book = book
#         self.pages = pages

#     def __add__(self, other):
#         return f"{self.book}&{other.book} with combine pages {self.pages+other.pages}"

# b1 = Book("Atomic Habits", 300)
# b2 = Book("Psychology of money", 200)

# print(b1+b2)




# class ShoppingCart:
#     def __init__(self, product, price):
#         self.product = product
#         self.price = price

#     def __add__(self, other):
#         t_product = f"{self.product} & {other.product}"
#         t_price = f"{self.price + other.price}"

#         return ShoppingCart(t_product, t_price)

#     def __str__(self):
#         return  f"Products Purchased : {self.product} | Total price : {self.price}"

# product_1 = ShoppingCart("T-shirt", 1000)
# product_2 = ShoppingCart("Track-pants", 1000)

# bill = product_1 + product_2
# print(bill)


class Vector:
    def __init__(self, *args):
        self.value = list(args)  # it will convert given value in list

    def __add__(self, other):
        addition = [x+y for x,y in zip(self.value, other.value)]
        return Vector(*addition)

    def __mul__(self, other):
        multiply = [x*y for x,y in zip(self.value, other.value)]
        return (sum(multiply))



    def __str__(self):
        return f"Vector{tuple(self.value)}"

v1 = Vector(1,2,7)
v2 = Vector(6,5,8)
v3 = Vector(2,4,9)
print(v1+v2+v3)
print(v1*v2)
