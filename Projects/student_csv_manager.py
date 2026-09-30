import csv
from pathlib import Path


# Get the folder containing this Python file
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# CSV file location
CSV_FILE = PROJECT_ROOT / "Resources" / "csv files" / "students.csv"


def initialize_database():
    """Create the CSV file and headers if it does not exist."""

    # Create the Resources/csv files directory if necessary
    CSV_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Create CSV file if it doesn't exist
    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["Name", "Grade", "Status"])


def add_student():
    """Add a new student to the CSV file."""

    name = input("Enter student name: ").strip()

    # Validate student name
    while not name:
        print("Student name cannot be empty.")
        name = input("Enter student name: ").strip()

    # Get and validate grade
    while True:
        try:
            grade = float(input("Enter student grade (0-100): "))

            if 0 <= grade <= 100:
                break

            print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Determine status
    if grade >= 50:
        status = "Passed"
    else:
        status = "Failed"

    # Save student
    with CSV_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([name, grade, status])

    print("\nStudent added successfully!")
    print(f"Name   : {name}")
    print(f"Grade  : {grade}")
    print(f"Status : {status}")


def view_students():
    """Display all saved student records."""

    with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        students = list(reader)

    if not students:
        print("\nNo student records found.")
        return

    print("\n" + "=" * 50)
    print("                 STUDENT RECORDS")
    print("=" * 50)

    print(f"{'Name':<25}{'Grade':<10}{'Status':<10}")
    print("-" * 50)

    for student in students:
        print(
            f"{student['Name']:<25}"
            f"{student['Grade']:<10}"
            f"{student['Status']:<10}"
        )

    print("=" * 50)


def main():
    """Run the Student CSV Manager."""

    initialize_database()

    while True:
        print("\n=============================")
        print("     Student CSV Manager")
        print("=============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        print("=============================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            print("\nThank you for using Student CSV Manager!")
            print("Goodbye! 👋")
            break

        else:
            print("\nInvalid choice.")
            print("Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()