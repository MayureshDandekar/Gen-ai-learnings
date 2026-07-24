# class BankAccount:

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
    
#     @property
#     def balance(self):
            # return self._balance

#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("amount cant be negative")
#         else :
#             self._balance = value
    
# try:
#     account = BankAccount("Mayuresh",-500)
#     print(account.balance)
# except ValueError as e:
#     print(f"Error: {e}")



class Product:
    def __init__(self, name , category, price, stock):
        self.name = name
        self._category = category
        self.price = price
        self.stock = stock

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Invalid Price")
        else:
            self.__price = value

    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock cant be negative")
        else:
            self.__stock = value

    def sell(self, quantity):
        if quantity > self.__stock:
            raise ValueError("Not enough stock")
        else:
            self.__stock -= quantity
            print(f"Available Stock is {self.__stock} and total sale value is {quantity*self.price}")
        
try:     
    p1 = Product("Tv", "Electronic", 1000, 20)
    print(p1.price)
except ValueError as e:
    print(f"Error: {e}")

try:     
    p1.sell(5)
except ValueError as e:
    print(f"Error: {e}")

try:     
    p1.price=-100
except ValueError as e:
    print(f"Error: {e}")

try:     
    p1.sell(100)
except ValueError as e:
    print(f"Error: {e}")