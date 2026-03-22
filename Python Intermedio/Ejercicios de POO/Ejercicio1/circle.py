#Cree una clase de Circle con:
#Un atributo de radius (radio).
#Un método de get_area que retorne su área.
import math

class Circle:
    radius = 4
    
    def get_area(self):
         return math.pi * (self.radius ** 2)

circle = Circle()
print("The area of your circle is ",circle.get_area())