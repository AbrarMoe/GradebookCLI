# main.py

import authentication
import student_manager
import statistics

def admin_menu():
    while True:
        print("\n*** Admin Menu ***")
        print("1. Add Student Record")
        print("2. Update Student Record")
        print("3. Delete Student Record")
        print("4. View Statistics")
        print("5. Sort Students")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            try:
                num_subjects = int(input("Enter number of subjects: ").strip())
            except ValueError:
                print("Invalid number!")
                continue
            grades_input = input("Enter grades separated by commas (e.g., 85,78,92,88): ").strip()
            try:
                grades = [float(g.strip()) for g in grades_input.split(",")]
                if len(grades) != num_subjects:
                    print("The number of grades does not match the number of subjects!")
                    continue
            except ValueError:
                print("Invalid grade input!")
                continue
            student_manager.add_student_record(student_id, name, grades)

        elif choice == "2":
            student_id = input("Enter Student ID to update: ").strip()
            rec = student_manager.get_student_record(student_id)
            if not rec:
                print("Student not found!")
                continue
            print(f"Current grades for {rec['name']}: {rec['grades']}")
            new_grades_input = input("Enter new grades separated by commas: ").strip()
            try:
                new_grades = [float(g.strip()) for g in new_grades_input.split(",")]
            except ValueError:
                print("Invalid input!")
                continue
            student_manager.update_student_record(student_id, new_grades)

        elif choice == "3":
            student_id = input("Enter Student ID to delete: ").strip()
            student_manager.delete_student_record(student_id)

        elif choice == "4":
            records = student_manager.load_student_records()
            statistics.generate_statistics(records)

        elif choice == "5":
            records = student_manager.load_student_records()
            if not records:
                print("No records to sort.")
                continue
            print("\nSort by:")
            print("1. GPA (highest first)")
            print("2. Name (alphabetical)")
            sort_choice = input("Enter your choice (1-2): ").strip()
            if sort_choice == "1":
                sorted_students = statistics.sort_students(records, sort_by='gpa')
            elif sort_choice == "2":
                sorted_students = statistics.sort_students(records, sort_by='name')
            else:
                print("Invalid choice.")
                continue
            print("\n=== Sorted Students ===")
            for student in sorted_students:
                print(f"ID: {student[0]}, Name: {student[1]}, GPA: {student[2]:.2f}")

        elif choice == "6":
            print("Exiting Admin Menu.")
            break

        else:
            print("Invalid choice. Try again.")

def student_menu(username):
    rec = student_manager.get_student_record(username)
    if rec:
        print(f"\n*** Student Record for {rec['name']} (ID: {username}) ***")
        print("Grades:", rec["grades"])
        gpa = statistics.compute_gpa(rec["grades"])
        print(f"GPA: {gpa:.2f}")
    else:
        print("Student record not found.")

def main():
    print("=== Student Grade Management System ===")
    
    # Predefined users
    users = {
        "admin": {"password": "adminpass", "role": "admin"},
        "student101": {"password": "studpass", "role": "student"},
        "student102": {"password": "studpass102", "role": "student"},
        "student103": {"password": "studpass103", "role": "student"},
        "student104": {"password": "studpass104", "role": "student"}
    }

    username, role = authentication.authenticate(users)
    if not username:
        return  # Stop if authentication fails

    if role == "admin":
        admin_menu()
    elif role == "student":
        student_menu(username)
    else:
        print("Unknown role encountered.")

if __name__ == "__main__":
    main()