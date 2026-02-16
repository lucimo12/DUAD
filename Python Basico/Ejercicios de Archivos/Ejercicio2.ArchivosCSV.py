#version alternativa
import csv

videogames = []

def videogames_info():
    total_videogames = int(input("How many videogames are you going to save today? "))
    counter = 0

    while counter < total_videogames:
        print(f"\nVideogame #{counter + 1}")

        game = {
            "name": input("Insert the name: "),
            "gender": input("Insert the gender: "),
            "developer": input("Insert the developer: "),
            "clasification": input("Insert the classification: ")
        }

        videogames.append(game)
        counter += 1


def write_tsv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(
            file,
            fieldnames=headers,
            delimiter='\t' 
        )
        writer.writeheader()
        writer.writerows(data)


videogames_headers = (
    "name",
    "gender",
    "developer",
    "clasification"
)

videogames_info()
write_tsv_file("videogames.tsv", videogames, videogames_headers)
