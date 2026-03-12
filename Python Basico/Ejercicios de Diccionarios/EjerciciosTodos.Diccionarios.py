#Cree un diccionario que guarde la siguiente información sobre un hotel:
#nombre
#numero_de_estrellas
#habitaciones

hotel_information = {
    'Name' : 'Four Seasons',
    'Star number' : 5,
    'Rooms' : 340
}

print(hotel_information)

#El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
#numero
#piso
#precio_por_noche

hotel_information = {
    'Name' : 'Four Seasons',
    'Star number' : 5,
    'Rooms' : [
        {
        'number' : 253,
        'floor' : 4,
        'price_per_night' : 200.000
}, 
        {
            'number' : 267, 
            'floor' : 5, 
            'price_per_night' : 500.000
            }
]
}

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

#Cree un programa que use una lista para eliminar keys de un diccionario.
#Ejemplos:
#list_of_keys = [’access_level’, ‘age’]
#employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}
#{’name’: ‘John’, 'email’: ‘john@ecorp.com’}

hotel_information = {
    'Name' : 'Four Seasons',
    'Location' : 'Miami',
    'Star number' : 5,
    'Rooms' : 340
}

list_of_keys = ['Location','Rooms']

deleted_item = {}

for key in list_of_keys:
    if key in hotel_information:
        deleted_item[key] = hotel_information[key]
        hotel_information.pop(key)

print(hotel_information)
print(f'Deleted items: {deleted_item}')