#Cree una clase de User que:
#Tenga un atributo de date_of_birth.
#Tenga un property de age.
#Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.
from datetime import datetime

def adult_only(func):
    def wrapper(*args, **kwargs):
        user = args[0]  # asumimos que el User es el primer parámetro

        if user.age < 18:
            raise Exception("You must be at least 18 years old")

        return func(*args, **kwargs)

    return wrapper


class User():
    date_of_birth = int
    
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
        
        
    @property
    def age(self):
        current_year = datetime.now().year
        return current_year - self.date_of_birth
    

    @adult_only
    def buy_tickets(self):
        return("Tickets purchased")
        


user1 = User(2000)
user2 = User (2010)

user1.buy_tickets()
user2.buy_tickets()