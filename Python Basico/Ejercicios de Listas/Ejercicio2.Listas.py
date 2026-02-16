#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

my_string = "Pizza con pepperoni"

for i in range(len(my_string)-1,-1,-1):
    print(f"{i}: {my_string[i]}")
# range(start, stop, step)
# start: len(my_string) - 1 → starts at the last index of the string
# stop: -1 → stops before index -1, so it includes index 0
# step: -1 → moves backwards through the string