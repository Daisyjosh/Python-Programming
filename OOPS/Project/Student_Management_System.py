class Student:
    def __init__(self,roll,name,marks):
        self.roll = roll
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Roll : {self.roll}, Name: {self.name}, Marks: {self.marks}")


class StudentMangementSystem:

    def __init__(self):
        self.students = []
    
    def add_students(self):
        roll = int(input("Enter Roll Number"))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))


        s = Student(roll,name,marks)
        self.students.append(s)
        print("Student added succesfully.\n")
    
    def display_all(self):
        if not self.students:
            print("No students avaiable.\n")
            return
        print("\n----Student List-----")
        for s in self.students:
            s.display()
        print()
    
    def search_student(self):
        roll = int(input("Enter roll number to search: "))

        for s in self.students:
            if s.roll == roll:
                print("Student Found: ")
                s.display()
                print()
                return
        print("Student not found\n")
    def delete_student(self):
        roll = int(input("Enter roll number to delete: "))

        for s in self.students:
            if s.roll == roll:
                self.students.remove(s)
                print("Student deleted\n")
                return
        print("Student not found.\n")
    
    def update_marks(self):
        roll = int(input("Enter roll number to update marks: "))

        for s in self.students:
            if s.roll == roll:
                new_marks = float(input("Enter new marks: "))
                s.marks = new_marks
                print("Marks updated successfully\n")
                return 
        print("Student not found\n")
def main():

    sms = StudentMangementSystem()

    while True:
        print("--Student Management System-----")
        print("1. Add Student")
        print("2. Display ALL students")
        print("3. Search Students")
        print("4. Update Marks")
        print("5. Delete Student Details")
        print("6. Exit")
        print()
        choice = input("Enter choice: ")
        if choice == "1":
            sms.add_students()
        elif choice == "2":
            sms.display_all()
        elif choice == "3":
            sms.search_student()
        elif choice == "4":
            sms.update_marks()
        elif choice =="5":
            sms.delete_student()
        elif choice == "6":
            print("Exiting program....")
            break
        else:
            print("Invalid choice. Try again.\n")
if __name__ == "__main__":
    main()