#Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

#La herencia múltiple permite combinar funcionalidades de varias clases en una sola.
# En este ejemplo, Coffee y Tea heredan de Beverage, Sugar y Milk 
# Lo que les permite reutilizar comportamientos como describir la bebida, 
# agregar azúcar y agregar leche sin duplicar código


class Beverage:
    def describe(self):
        return "This is a beverage"


class Sugar:
    def add_sugar(self):
        return "Sugar added"


class Milk:
    def add_milk(self):
        return "Milk added"


class Coffee(Beverage, Sugar, Milk):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name

class Tea(Beverage, Sugar, Milk):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name

coffee1 = Coffee("Latte")
coffee2 = Coffee("Americano")

tea1 = Tea("Chai")

print(coffee1)
print(coffee1.describe())
print(coffee1.add_sugar())
print(coffee1.add_milk())

print(coffee2)
print(coffee2.add_sugar())

print(tea1)
print(tea1.add_milk())