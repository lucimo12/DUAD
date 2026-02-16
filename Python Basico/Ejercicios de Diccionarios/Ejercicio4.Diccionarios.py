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