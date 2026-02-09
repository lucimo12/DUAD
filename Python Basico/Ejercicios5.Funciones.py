#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def show_name():
    print("Mi nombre es Lucia")

    
def show_age():
    print("Mi edad es 24")
    show_name()
show_age()

#Experimente con el concepto de scope:
#Intente accesar a una variable definida dentro de una función desde afuera.

def lucia_info():
    name = "Lucia"
    age = 24
    print("Esta es la info: ", "nombre: ",name, "edad:",age)
    
lucia_info()
#print("Esta es la info: ", "nombre: ",name, "edad:",age)


#Intente accesar a una variable global desde una función y cambiar su valor.

number_sum = 9

def number():
    global number_sum
    number_sum = 4
    print("The total is:", number_sum)

number()
print(number_sum)


#Cree una función que retorne la suma de todos los números de una lista.
#La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#[4, 6, 2, 29]

my_list = [4, 6, 2, 29]

def sum_list(my_list):
    total = 0
    for x in my_list:
        total = total + x
    return total

result = sum_list(my_list)
print(result)

#Cree una función que le de la vuelta a un string y lo retorne.
#Esto ya lo hicimos en iterables.
#“Hola mundo” → “odnum aloH”


def word_change():
    my_string = "Hola mundo"
    for i in range(len(my_string)-1,-1,-1):
        print(f"{i}: {my_string[i]}")
word_change()

#Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

text = "I love Nacion Sushi"

def string_info(text):
    upper_cases = 0 #tienen que ir como variables locales 
    lower_cases = 0
    for x in text: 
        if x.isupper():
            upper_cases += 1
        elif x.islower():
            lower_cases += 1
    print("There's",upper_cases,"upper cases and ",lower_cases,"lower cases")
string_info(text)

#Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
text_original = "python-variable-funcion-computadora-monitor"

def string_order(text):
    words = text.split("-")
    order = sorted(words)
    result = "-".join(order)  
    return result

print(string_order(text_original))
    
#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar otra función para revisar si el numero es primo o no.

new_list = [1, 4, 6, 7, 13, 9, 67]

def prime_number(x):
    if x <= 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True

def prime_list(numbers):
    primes = []

    for n in numbers:
        if prime_number(n):
            primes.append(n)

    return primes

result = prime_list(new_list)
print(result)