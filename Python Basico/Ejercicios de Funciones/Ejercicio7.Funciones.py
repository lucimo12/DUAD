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