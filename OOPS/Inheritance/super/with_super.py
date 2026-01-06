class Person:
    def __init__(self):
        print("Parent Constructor")

class Student(Person):
    def __init__(self):
        super().__init__()
        print("Child Constructor")