import csv
import os

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
        writer.writerows(students_list)

    print(f"Data exported successfully to {CSV_FILE}")


def import_from_csv():
    if not os.path.exists(CSV_FILE):
        print("No previously exported file was found.")
        return []

    students_list = []
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert grades back to int
            row["spanish"] = int(row["spanish"])
            row["english"] = int(row["english"])
            row["social"] = int(row["social"])
            row["science"] = int(row["science"])
            students_list.append(row)

    print(f"Data imported successfully from {CSV_FILE}")
    return students_list