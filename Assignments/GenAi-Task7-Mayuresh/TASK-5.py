from abc import ABC , abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self , amount):
        pass

class CreditCardPayment(Payment):

    def process_payment(self, amount):
        print(f"{amount} is debited from Your Credit Card")

class UpiPayment(Payment):

    def process_payment(self, amount):
        print(f"{amount} is credited from Your Upi account")


transaction_1 = CreditCardPayment()
transaction_2 = UpiPayment()
transaction_1.process_payment(1000)
transaction_2.process_payment(7000)
