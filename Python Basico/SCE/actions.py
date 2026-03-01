students_list = [] 

def save_information(students_list): 
    counter = 0
    student_amount = int(input("How many students are you going to add today? "))
    
    
    while counter < student_amount:
        student = {} 
        
        
        name = input("\nWhat's the student name? ") 
        student["name"] = name
        
        section = input("What's the section? ")
        student["section"] = section
        
        spanish_grade = get_valid_grade("spanish")
        student["spanish grade"] = spanish_grade
        
        english_grade = get_valid_grade("english")
        student["english grade"] = english_grade
        
        social_grade = get_valid_grade("social")
        student["social grade"] = social_grade
        
        science_grade = get_valid_grade("science")
        student["science grade"] = science_grade
        
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


