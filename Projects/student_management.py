students = {} # Key: Name, Value: List of Marks

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student & Grade")
    print("2. View All Students")
    print("3. Find Student Average")
    print("4. Exit")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        name = input("Enter student name: ").strip()
        grade = float(input(f"Enter grade for {name}: "))
        if name in students:
            students[name].append(grade)
        else:
            students[name] = [grade]
        print("Record updated!")
        
    elif choice == "2":
        print("\nStudent Records:")
        for name, grades in students.items():
            print(f"{name}: {grades}")
            
    elif choice == "3":
        name = input("Enter name to calculate average: ")
        if name in students:
            avg = sum(students[name]) / len(students[name])
            print(f"{name}'s Average Grade: {avg:.2f}")
        else:
            print("Student not found.")
            
    elif choice == "4":
        print("Goodbye!")
        break
