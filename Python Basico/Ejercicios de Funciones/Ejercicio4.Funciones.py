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