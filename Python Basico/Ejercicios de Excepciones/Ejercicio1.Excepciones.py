#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

print("Hi, welcome to your online calculator")


def ask_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Error: it has to be a valid number")


def show_menu():
    while True:
        try:
            return int(input(
                "This are your options:\n"
                "1. Sum\n"
                "2. Rest\n"
                "3. Multiplication\n"
                "4. Division\n"
                "5. Erase result\n"
                "6. Exit\n"
                "Choose an option: "
            ))
        except ValueError:
            print("Error: you have to choose a number from the menu")


def sum(actual):
    number = ask_number("Write the second number: ")
    return actual + number


def rest(actual):
    number = ask_number("Write the second number: ")
    return actual - number


def multiplication(actual):
    number = ask_number("Write the second number: ")
    return actual * number


def division(actual):
    number = ask_number("Write the second number: ")
    if number == 0:
        print("It cant be 0")
        return actual
    return actual / number


def calculator():
    number_actual = ask_number("Write the second number: ")

    while True:
        print("\nNumber actual:", number_actual)

        option = show_menu()

        if option == 1:
            number_actual = sum(number_actual)

        elif option == 2:
            number_actual = rest(number_actual)

        elif option == 3:
            number_actual = multiplication(number_actual)

        elif option == 4:
            number_actual = division(number_actual)

        elif option == 5:
            number_actual = 0
            print("Result erased.")

        elif option == 6:
            print("Exit from calculator.")
            break

        else:
            print("Invalid option.")


calculator()
