#Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

print("Hola" + " Mundo") #se suma 
print("Hola" + 5) #da error porque no se puede sumar string con int
print(5 + "Hola") #da error porque no se puede sumar string con int
print([1, 2, 3] + [4, 5, 6]) #se suma 
print("Hola" + [1, 2, 3]) #error, no se puede sumar string con lista
print(2.5 + 2) #se suma
print(True + True)   #da resultado 2
print(True + False)  #da resultado 1
print(False + False) #da resultado 0



#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
name = input("What's your name?")
last_name = input("What's your last name?")
age = int(input("What's your age?"))
if (age < 5 ):
    print("Baby")
elif (age < 12):
    print("Kid")
elif(age < 18 ):
    print("Teenager")
elif(age < 30):
    print("Young adult")
elif(age < 60):
    print("Adult")
else:
    print("Elderly")


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
    
#Dada n cantidad de notas de un estudiante, calcular:
##Cuantas notas tiene aprobadas (mayor a 70).
#Cuantas notas tiene desaprobadas (menor a 70).
#El promedio de todas.
#El promedio de las aprobadas.
#El promedio de las desaprobadas.

grades_counter = 1
passed_grades = 0
failed_grades = 0
sum_passed_grades = 0
sum_failed_grades = 0
sum_all_grades = 0
grades_total = int(input("How many grades do you have? "))

while grades_counter <= grades_total:
    print("Insert the grade number:", grades_counter)
    grade = int(input("Whats your grade? "))
    grades_counter = grades_counter + 1

    sum_all_grades = sum_all_grades + grade

    if grade < 70:
        failed_grades = failed_grades + 1
        sum_failed_grades = sum_failed_grades + grade
    else:
        passed_grades = passed_grades + 1
        sum_passed_grades = sum_passed_grades + grade


if failed_grades > 0:
    average_failed_grades = sum_failed_grades / failed_grades
else:
    average_failed_grades = 0

if passed_grades > 0:
    average_passed_grades = sum_passed_grades / passed_grades
else:
    average_passed_grades = 0

average_grades = sum_all_grades / grades_total


print("The student has this amount of grades approved:", passed_grades)
print("This is the average of passed grades:", average_passed_grades)
print("The student has this amount of grades failed:", failed_grades)
print("This is the average of failed grades:", average_failed_grades)
print("This is the average of the grades:", average_grades)