#Cree una clase de Bus con:
#1.Un atributo de max_passengers.
#2.Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
#3.Un método para bajar pasajeros uno por uno (en cualquier orden).

class Bus:
    def __init__(self, max_passengers):
        self.passengers = []
        self.max_passengers = max_passengers
    
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

class Person():
    def __init__(self, name):
        self.name = name
        
        
bus1 = Bus(40)
#bus2 = Bus(20)

person1 = Person("Lucia")
person2 = Person("Juan")

#person3 = Person("Maria")

bus1.add_passenger(person1)
bus1.add_passenger(person2)

#bus2.add_passenger(person3)

for p in bus1.passengers:
    print(p.name)
    
#for x in bus2.passengers:
    #print(x.name)