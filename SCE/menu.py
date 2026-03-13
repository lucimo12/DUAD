from actions import (
    save_information,
    student_info,
    top_average,
    general_average
)

from data import (
    export_to_csv,
    import_from_csv
)



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
            if 1 <= option <= 7:
                return option
            else:
                print("Error: choose a number from 1 to 7.")

        except ValueError:
            print("Error: you have to choose a number from the menu")
        
            

def menu_main():
    students_list = []
    
    while True:
        option = show_menu()
        
        if option == 1:
            save_information(students_list)

        elif option == 2:
            student_info(students_list)

        elif option == 3:
            top_average(students_list)

        elif option == 4:
            general_average(students_list)

        elif option == 5:
            export_to_csv(students_list)

        elif option == 6:
            imported = import_from_csv()
            if len(imported) > 0:
                students_list = imported

        elif option == 7:
            print("Goodbye!")
            break
        
        
