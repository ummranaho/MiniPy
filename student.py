class Student:
    def __init__(self,  student_id,name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.student_id = student_id
    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print("-----------------------------")

class StudentManagementSystem:
    def __init__(self):
        self.students =[]

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        student = Student(student_id, name, age, course)
        self.students.append(student)
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                student.display_info()
    def search_student(self):
        sid = input("Enter student ID to search: ")
        for student in self.students:
            if student.student_id == sid:
                student.display_info()
                return
        print("Student not found.")
        
    def update_student(self):
        sid = input ("Enter Student ID to update:")
        for student in self.students:
            if student.student_id == sid:
                name = input("Enter new name: ")
                age = int(input("Enter new age: "))
                course = input("Enter new course: ")
                student.name = name
                student.age = age
                student.course = course
                print("Student information updated successfully.")
                return
        print("Student not found.")
    def delete_student(self):
        sid = input("Enter student ID to delete: ")
        for student in self.students:
            if student.student_id == sid:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")
def main():
    system = StudentManagementSystem()
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.view_students()
        elif choice == "3":
            system.search_student()
        elif choice == "4":
            system.update_student()
        elif choice == "5":
            system.delete_student()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")

main()

