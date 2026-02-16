
#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
#Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
import random
number = int(input("Insert a number"))
random_number = random.randint(1, 10)

while (number != random_number):
    print("Sorry, try again")
    number = int(input("Insert a number"))
print("Congrats, its correct")
    
#Cree un programa que le pida tres números al usuario y muestre el mayor.
number_one = int(input("Insert a number"))
number_two = int(input("Insert a number")) 
number_three = int(input("Insert a number "))
if (number_one > number_two and number_one > number_three):
    print(number_one)
elif (number_two > number_one and number_two > number_three):
    print(number_two)
else:
    print(number_three)
    