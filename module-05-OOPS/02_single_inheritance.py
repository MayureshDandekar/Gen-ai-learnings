class Animal():

    def __init__(self,name):
        self.name = name 

    def speak(self):
        print(f"{self.name} is saying ")

class Dog(Animal):

    def __init__(self, name , breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} is saying woof!")

    def fetch(self):
        print(f"{self.name} is fetching")

tom = Dog("Tom", "Labrador")
tom.speak()
tom.fetch()