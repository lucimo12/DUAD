#Dada n cantidad de notas de un estudiante, calcular:
##Cuantas notas tiene aprobadas (mayor a 70).
#Cuantas notas tiene desaprobadas (menor a 70).
#El promedio de todas.
#El promedio de las aprobadas.
#El promedio de las desaprobadas.

grades_counter = 1
passed_grades = 0
failed_grades = 0
sum_passed_grades = 0
sum_failed_grades = 0
sum_all_grades = 0
grades_total = int(input("How many grades do you have? "))

while grades_counter <= grades_total:
    print("Insert the grade number:", grades_counter)
    grade = int(input("Whats your grade? "))
    grades_counter = grades_counter + 1

    sum_all_grades = sum_all_grades + grade

    if grade < 70:
        failed_grades = failed_grades + 1
        sum_failed_grades = sum_failed_grades + grade
    else:
        passed_grades = passed_grades + 1
        sum_passed_grades = sum_passed_grades + grade


if failed_grades > 0:
    average_failed_grades = sum_failed_grades / failed_grades
else:
    average_failed_grades = 0

if passed_grades > 0:
    average_passed_grades = sum_passed_grades / passed_grades
else:
    average_passed_grades = 0

average_grades = sum_all_grades / grades_total


print("The student has this amount of grades approved:", passed_grades)
print("This is the average of passed grades:", average_passed_grades)
print("The student has this amount of grades failed:", failed_grades)
print("This is the average of failed grades:", average_failed_grades)
print("This is the average of the grades:", average_grades)