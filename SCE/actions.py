def save_information(students_list): 
    counter = 0
    student_amount = int(input("How many students are you going to add today? "))
    
    
    while counter < student_amount:
        student = {} 
        
        
        name = input("\nWhat's the student name? ") 
        student["name"] = name
        
        section = input("What's the section? ")
        student["section"] = section
        
        student["spanish"] = get_valid_grade("spanish")
        student["english"] = get_valid_grade("english")
        student["social"] = get_valid_grade("social")
        student["science"] = get_valid_grade("science")

        students_list.append(student)
        
        print(f"Student {name} has been added successfully")
        counter += 1
    return students_list

def get_valid_grade(subject):
    while True:
        try:
            grade = int(input(f"What's the {subject} grade? "))
            
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_average(student):
    total = (
        student["spanish"] +
        student["english"] +
        student["social"] +
        student["science"]
    )
    return total / 4

def student_info(students_list):
    if len(students_list) == 0:
        print("No students added yet.")
        return

    for student in students_list:
        avg = calculate_average(student)
        print("\nName:", student["name"])
        print("Section:", student["section"])
        print("Spanish:", student["spanish"])
        print("English:", student["english"])
        print("Social:", student["social"])
        print("Science:", student["science"])
        print("Average:", round(avg, 2))

def top_average(students_list):
    if len(students_list) == 0:
        print("You need to add a student")
        return
    
    ordered = sorted(students_list, key=calculate_average, reverse=True )
    top = ordered[:3]

    print("\nTop 3 Students:")
    for i, student in enumerate(top, start=1):
        avg = calculate_average(student)
        print(f"{i}. {student['name']} - Average: {round(avg, 2)}")
    
    
def general_average(students_list):
    if len(students_list) == 0:
        print("No students added yet.")
        return

    total = 0
    for student in students_list:
        total += calculate_average(student)

    group_avg = total / len(students_list)
    print("General average of all students:", round(group_avg, 2))