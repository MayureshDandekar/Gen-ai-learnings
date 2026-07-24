from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" in value:
            self.__email = value
        else:
            raise ValueError("Invalid email")
    def send(self, message):
        return (f"Emailng.. {self.email}: {message}")


class SMSNotifier(Notifier):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if len(str(value)) !=10 or not str(value).isdigit():
            raise ValueError("Invalid Phone number")
        self.__phone_number = value

    def send(self, message):
        return f"Texting.. {self.phone_number} : {message}"


class PushNotifier(Notifier):
    def __init__(self, devise_id):
        self._devise_id = devise_id
    def send(self, message):
        return f"Push to devise {self._devise_id}: {message}"


try:
    notifiers = [EmailNotifier("test@email.com"), SMSNotifier("12345678a90"), PushNotifier("dev123")]
    for n in notifiers:
        print(n.send("server is down"))
except ValueError as e :
    print(f"Error: {e}") 