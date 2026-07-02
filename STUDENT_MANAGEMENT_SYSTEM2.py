# Initialize data structures
students = []
all_subjects = set()

while True:
    print("\n---------------------------------------------------------- STUDENT DATA ORGANIZER ------------------------------------------------------------")
    # Print Option Menu Reference
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    # =============================================================
    choice = int(input("Choose option: "))

    if choice == 1:
        print("\n--- Add New Student ---")
        
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))  # type casting
        grade = input("Enter grade: ")
        subjects_input = input("Enter subjects (comma-separated): ")
        
        subjects = [sub.strip() for sub in subjects_input.split(",")]
        all_subjects.update(subjects)  # adding to set
        
        student_id = input("Enter student ID: ")
        dob = input("Enter date of birth (DD-MM-YYYY): ")
        
        # Tuple (immutable data)
        student_identity = (student_id, dob)
        
        # Dictionary to store student data
        student_record = {
            "identity": student_identity,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }
        
        students.append(student_record)  # list is mutable
        print(f"\nStudent {name} added successfully!")


    # =============================================================
    elif choice == 2:
        print("\n--- All Student Records ---")
        
        if not students:
            print("......No student records found.......")
        
        for student in students:
            sid, dob = student["identity"]
            
            # f-string formatting
            print(f"""
    Student ID : {sid}
    Name       : {student['name']}
    Age        : {student['age']}
    Grade      : {student['grade']}
    Subjects   : {", ".join(student['subjects'])}
    DOB        : {dob}
    """)

    # =============================================================
    elif choice == 3:
        print("\n--- Update Student Information ---")
        sid = input("Enter student ID to update: ")
        
        for student in students:
            # Checking against the first element of our identity tuple (student_id)
            if student in students and student["identity"][0] == sid:
                print("1. Update Age")
                print("2. Update Subjects")
                choice = int(input("Choose option: "))
                
                if choice == 1:
                    student["age"] = int(input("Enter new age: "))
                    print("Age updated successfully.")
                    
                elif choice == 2:
                    new_subjects = input("Enter new subjects (comma-separated): ")
                    subjects_list = [s.strip() for s in new_subjects.split(",")]
                    student["subjects"] = subjects_list
                    all_subjects.update(subjects_list)
                    print("Subjects updated successfully.")
            else:
                print(".......Student ID not found......")

    # =============================================================
    elif choice == 4:
        print("\n--- Delete Student ---")
        sid = input("Enter student ID to delete: ")
        
        for i, student in enumerate(students):
            if student["identity"][0] == sid:
                del students[i]  # using del keyword
                print(".......Student record deleted......")

    #=============================================================

    elif choice == 5:
        print("\n--- Subjects Offered ---")
        for subject in all_subjects:
            print(subject)

    #============================================================

    elif choice == 6:
        print("\nThank you for using the Student Data Organizer!")
        break

    else:
        print("........Invalid choice. Try again......")
        break