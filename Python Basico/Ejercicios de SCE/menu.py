#Ingresar información de n cantidad de estudiantes, uno por uno.
#Cada estudiante debe incluir:
#Nombre completo
#Sección (ejemplo: 11B)
#Nota de español
#Nota de inglés
#Nota de sociales
#Nota de ciencias


def student_grades():
    counter = 0
    student_amount = int(input("How many students are you going to add today? "))
    while counter < student_amount:

        
        name = input("What's the student name? ") 
        section = input("What's the section? ")
        spanish_note = int(input("What's the spanish note? "))
        english_note = int(input("What's the english note? "))
        social_note = int(input("What's the social note? "))
        science_note = int(input("What's the science note? "))
        print("Student has been added successfully")
        counter += 1

student_grades()

def student_info():
    

def show_menu():
    while True:
        try:
            return int(input(
                "This are your options:\n"
                "1. Add student information\n"
                "2. Show student list information\n"
                "3. Show top 3 students with the best grade average\n"
                "4. Show students average grade\n"
                "5. Export information to an CSV archive\n"
                "6. Import the CSV archive previously created \n"
                "7. Exit\n"
                "Choose an option: "
            ))
        except ValueError:
            print("Error: you have to choose a number from the menu")
            

def menu_main():
    option = show_menu()
    
    if option == 1:
        student_grades()
    elif option == 2:
        student_info()
    elif option == 3:
    elif option == 4:
    elif option == 5:
    elif option == 6:
    elif option == 7:
        