class Livingthing():
    def breath(self):
        return "Breathing"

class Animal(Livingthing):
    def move(self):
        return "Moving"

class Dog(Animal):
    def bark(self):
        return "Woof" 

tom = Dog()
print(tom.breath())
print(tom.move())
print(tom.bark())