
#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#Ejemplos:
#list_a = [’first_name’, ‘last_name’, ‘role’]
#list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]
# {’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}

list_a = ['color','food','sport']
list_b = ['blue','pizza','gym']

diccionario = {}
    
for i in range(len(list_a)):
    diccionario[list_a[i]] = list_b[i]
    
print(diccionario)