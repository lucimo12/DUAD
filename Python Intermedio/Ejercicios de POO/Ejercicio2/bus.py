#Cree una clase de Bus con:
#1.Un atributo de max_passengers.
#2.Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
#3.Un método para bajar pasajeros uno por uno (en cualquier orden).

class Bus:
    max_passengers = 40
    passengers = []
    
    class Person():
        def __init__(self, name):
            self.name = name
    
    def add_passenger(self, person):
        actual_passengers = len(self.passengers)
        if actual_passengers >= self.max_passengers:
            print("Bus is full")
        else: 
            self.passengers.append(person)
        
    def rest_passenger(self):
        if len(self.passengers) > 0:
            self.passengers.pop()
        else:
            print("No passengers to remove")

bus = Bus()

person1 = "Lucia"
person2 = "Juan"

bus.add_passenger(person1)
bus.add_passenger(person2)
print("Passengers: ", bus.passengers)