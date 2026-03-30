#Cree una clase abstracta de Shape que:
#Tenga los métodos abstractos de calculate_perimeter y calculate_area.
#Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
#Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    def calculate_area(self):
        pass
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()
    
    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return area
    

class Square(Shape):
    def __init__(self, side):
        self.side = side
        super().__init__()
    
    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter
    
    def calculate_area(self):
        area = self.side ** 2
        return area
    
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__()
    
    def calculate_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
    
    def calculate_area(self):
        area =  self.width * self.height
        return area

circle1 = Circle(4)

print("Area: ", circle1.calculate_area())
print("Perimeter: ", circle1.calculate_perimeter())


square1 = Square(4)
print("Area: ", square1.calculate_area())
print("Perimeter: ", square1.calculate_perimeter())

rectangle1 = Rectangle(2,5)
print("Area: ", rectangle1.calculate_area())
print("Perimeter: ", rectangle1.calculate_perimeter())



