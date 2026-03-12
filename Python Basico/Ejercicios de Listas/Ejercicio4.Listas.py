#Cree un programa que elimine todos los números impares de una lista.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [] 
for i in my_list:
    if i % 2 == 0: 
        new_list.append(i)
print("Los numeros pares son:",new_list)