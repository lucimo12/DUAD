#Cree un programa que:
#Pida al usuario su nombre
#Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")


while True:
        name = input("Digita tu nombre: ")

        if name.isdigit():
            raise ValueError("El nombre no puede ser un número")

        print(f"Hola {name}")
        break

#Luego pida su edad
#Si no es un número válido, capture el ValueError y muestre un mensaje

while True:
    try:
        age = int(input("Digita tu edad: "))

        if age <= 0:
            print("La edad debe ser un número positivo")
            continue

        print(f"Tienes {age} años")
        break

    except ValueError:
        print("La edad debe ser un número válido")

print(f"Hola {name}, tu edad es {age}")
