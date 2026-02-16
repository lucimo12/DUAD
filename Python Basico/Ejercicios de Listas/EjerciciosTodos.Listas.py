#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
#first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]
#second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

for i in range(len(first_list)): # 'i' represents the index position.The loop runs from 0 to the length of the list.
    print(f"{i}: {first_list[i]}, {second_list[i]}") #{i} prints the current index.
# {first_list[i]} prints the element of the first list at index i.
# {second_list[i]} prints the element of the second list at index i.


#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

my_string = "Pizza con pepperoni"

for i in range(len(my_string)-1,-1,-1):
    print(f"{i}: {my_string[i]}")
# range(start, stop, step)
# start: len(my_string) - 1 → starts at the last index of the string
# stop: -1 → stops before index -1, so it includes index 0
# step: -1 → moves backwards through the string

#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
my_list = [4, 3, 6, 1, 7]

temp = my_list[0] #if I dont save the number and switched it, it will be lost. 
my_list[0] = my_list[len(my_list)-1]
my_list[len(my_list)-1] = temp
print(my_list)

#Cree un programa que elimine todos los números impares de una lista.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [] 
for i in my_list:
    if i % 2 == 0: 
        new_list.append(i)
print("Los numeros pares son:",new_list)

#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
counter = 1
number_list = []
while counter < 11:
    number_list.append(int(input("Write a number")))
    counter = counter + 1
print(number_list)
highest = number_list[0]
for number in number_list:
    if number > highest:
        highest = number

print("The highest number is:", highest)