#Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
#Debe incluir:
#Nombre
#Género
#Desarrollador
#Clasificación ESRB
import csv

videogames = []

def videogames_info():
    total_videogames = int(input("How many videogames are you going to save today? "))
    counter = 0
    
    while counter < total_videogames:
        game = {
        "name" : input("Insert the name: "),
        "gender" : input("Insert the gender: "),
        "developer" : input("Insert the developer: "),
        "clasification" : input("Insert the calification: ")
    }
        print("You have saved a new game")
        videogames.append(game)
        counter +=1


def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)

videogames_headers = (
    "name",
    "gender",
    "developer",
    "clasification"
)

videogames_info()
write_csv_file("videogames.csv", videogames, videogames_headers)
