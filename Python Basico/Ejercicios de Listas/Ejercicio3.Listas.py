#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
my_list = [4, 3, 6, 1, 7]

temp = my_list[0] #if I dont save the number and switched it, it will be lost. 
my_list[0] = my_list[len(my_list)-1]
my_list[len(my_list)-1] = temp
print(my_list)