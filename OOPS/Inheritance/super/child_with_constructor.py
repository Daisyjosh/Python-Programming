class Person:
    def __init__(self):
        print("Parent Constructor..")

class Student(Person):
    def __init__(self):
        print("Child Constructor..")

s = Student() # Only Child constructor called parent constructor can't be called automatically 
# Hence use super()