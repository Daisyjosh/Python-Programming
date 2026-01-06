class person:
    def __init__(self):
        print("Parent Constructor")

class Student(person):
    pass # Parent constructor called automatically 

s = Student()


