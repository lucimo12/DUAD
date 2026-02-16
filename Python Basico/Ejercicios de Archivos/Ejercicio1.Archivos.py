#Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def read_songs_from_file(file_path):
    with open(file_path, 'r') as file:
        songs = file.readlines()
    return songs

def write_list_to_file(file_path, song_list):
    with open(file_path, 'w') as file:
        for song in song_list:
            file.write(song + "\n")

songs = read_songs_from_file("songs.txt")

songs = [song.strip() for song in songs]

songs.sort()

write_list_to_file("songs_sorted.txt", songs)