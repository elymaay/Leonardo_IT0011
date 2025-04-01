students = []

while True:
    print("\nMenu:")
    print("1. Show All Students Record")
    print("2. Order by Last Name")
    print("3. Order by Grade")
    print("4. Show Student Record")
    print("5. Add Record")
    print("6. Edit Record")
    print("7. Delete Record")
    print("8. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        for student in students:
            print(student)
    
    if choice == '2':
        sorted_students = sorted(students, key=lambda x: x[1][1])
        for student in sorted_students:
            print(student)
    
    if choice == '3':
        sorted_students = sorted(students, key=lambda x: (0.6 * x[2] + 0.4 * x[3]), reverse=True)
        for student in sorted_students:
            print(student)
    
    if choice == '4':
        student_id = input("Enter Student ID: ")
        found = False
        for student in students:
            if student[0] == student_id:
                print(student)
                found = True
        if not found:
            print("Student not found.")
    
    if choice == '5':
        student_id = input("Enter Student ID (6 digits): ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam = float(input("Enter Major Exam Grade: "))
        students.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully.")
    
    if choice == '6':
        student_id = input("Enter Student ID to edit: ")
        found = False
        for i in range(len(students)):
            if students[i][0] == student_id:
                print("Editing Record: ", students[i])
                first_name = input("Enter New First Name: ")
                last_name = input("Enter New Last Name: ")
                class_standing = float(input("Enter New Class Standing Grade: "))
                major_exam = float(input("Enter New Major Exam Grade: "))
                students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
                print("Record updated successfully.")
                found = True
        if not found:
            print("Student not found.")
    
    if choice == '7':
        student_id = input("Enter Student ID to delete: ")
        found = False
        for student in students:
            if student[0] == student_id:
                students.remove(student)
                print("Record deleted successfully.")
                found = True
        if not found:
            print("Student not found.")
    
    if choice == '8':
        print("Exiting...")
        break
    
    if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        print("Invalid choice, please try again.")