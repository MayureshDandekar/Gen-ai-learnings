class Avengers():
    def __init__(self,name , power, nationality):
        self.name = name 
        self.power = power
        self.nationality = nationality

    def introduction(self):
        print(f"Hello it me {self.name}, my power is {self.power}, and i am from {self.nationality}")

shaktiman = Avengers("Shaktiman", "Combat fighting", "India")
shaktiman.introduction()