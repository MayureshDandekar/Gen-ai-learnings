# Polymorphism

# 1. Method Overriding

import math

class Shape:

    def area(self):
        return 0

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius*self.radius
    

for shape in [Rectangle(7,8), Circle(7)]:
    print(shape.area()) 


# 2. Method Overloading

class Calculator:

    def area(self, *args):
        if len(args)==1:
            return args[0]*args[0]
        elif len(args)==2:
            return args[0]*args[1]
        else:
            return None

o = Calculator()

print(o.area(4))
print(o.area(4,3))


# 3. Duck typing

#Book() creates an object, that object gets passed into get_info as item, and Python runs Book's describe()
#because the object carries its class internally — not because you wrote the word Book anywhere near the function call.
class Book:
    def describe(self):
        print("Book:Atomic Habits, Author:James Clear")

class Movie:
    def describe(self):
        print("Movie:Dhurander, Actor:Ranveer")

class Song:
    def describe(self):
        print("Song:KabhiKabhi, Singer:KishorKumar")

def get_info(item):
    item.describe()

get_info(Book())
get_info(Movie())
get_info(Song())