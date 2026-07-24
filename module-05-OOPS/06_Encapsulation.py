# # Public
# # Accessible from anywhere. acc.balance works fine, no restriction at all.
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance 

acc = Account("Mayuresh", 1000000)
print(acc.balance)

# Protected
# Convention says: "this is internal — meant for use inside this class or subclasses only, outside code shouldn't touch it." 
# But nothing stops you — acc._balance still works. It's a signal to other developers, not an enforced rule. 
# Python trusts you to respect the underscore.
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance 

acc = Account("Mayuresh", 1000000)
print(acc._balance)


# Private
# This one actually does something mechanically — Python name-mangles it. self.__balance internally becomes self._Account__balance. 
# So acc.__balance from outside throws AttributeError — not because Python blocked it, 
# # but because the name literally changed under the hood and you're looking for the wrong name. 
# # Determined code can still access acc._Account__balance directly. Still not a real wall — just a taller fence.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance 

acc = Account("Mayuresh", 1000000)
print(acc._Account__balance) # we can access this way also from outside the class









class BankAccount:

    def __init__(self, owner, balance, branch):
        self.owner = owner
        self.__balance = balance # Private
        self._branch = branch    # Protected

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Balance Insufficient")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Mayuresh", 1000, "Pune")
acc.deposit(100)
acc.withdraw(5000)
print(acc.get_balance())
# print(acc._BankAccount__balance)

