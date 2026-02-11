#Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON
#Debe leer el archivo para importar los Pokémones existentes.
#Luego debe pedir la información del Pokémon a agregar.
#Finalmente debe guardar el nuevo Pokémon en el archivo.


import json

with open("pokemon.json", "r", encoding="utf-8") as file:
    pokemons = json.load(file)


name = input("Name: ")
level = int(input("Level: "))
types_input = input("Types (if more than one separate the values with a comma): ")
types_list = [t.strip() for t in types_input.split(",")]

hp = int(input("HP: "))
attack = int(input("Attack: "))
defense = int(input("Defense: "))
sp_attack = int(input("Sp. Attack: "))
sp_defense = int(input("Sp. Defense: "))
speed = int(input("Speed: "))



new_pokemon = {
    "name": {"english": name},
    "level": level,
    "type": types_list,
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
    }
}


pokemons.append(new_pokemon)


with open("pokemon.json", "w", encoding="utf-8") as file:
    json.dump(pokemons, file, indent=2, ensure_ascii=False)

print("Pokémon agregado correctamente")
