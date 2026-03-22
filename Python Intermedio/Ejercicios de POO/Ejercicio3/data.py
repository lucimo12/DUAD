import csv
import os
from student import Student

CSV_FILE = "students.csv"


def export_to_csv(students_list):
    if len(students_list) == 0:
        print("No students to export.")
        return

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "section", "spanish", "english", "social", "science"]
        )
        writer.writeheader()

        for student in students_list:
            writer.writerow(student.to_dict())

    print(f"Data exported successfully to {CSV_FILE}")


def import_from_csv():
    if not os.path.exists(CSV_FILE):
        print("No previously exported file was found.")
        return []

    students_list = []
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students_list.append(
                Student(
                    row["name"],
                    row["section"],
                    int(row["spanish"]),
                    int(row["english"]),
                    int(row["social"]),
                    int(row["science"])
                )
            )

    print(f"Data imported successfully from {CSV_FILE}")
    return students_list