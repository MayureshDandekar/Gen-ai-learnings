import math
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"The area of rectangle is {self.width*self.height}"
    
    def perimeter(self):
        return f"The perimeter of rectangle is {2*(self.width+self.height)}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"The area of circle is {math.pi*self.radius*self.radius}"
    
    def perimeter(self):
        return f"The perimeter of circle is {2*(math.pi*self.radius)}"

# for shape in [Rectangle(7,7), Circle(7)]:
#     print(shape.area() )
#     print(shape.perimeter())

o=Shape()
o.area() 