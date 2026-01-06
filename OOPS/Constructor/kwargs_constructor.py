class Student:
    def __init__(self, **info):
        # We are just printing what is passed in the info
        # If we self.info we usually print what stored in that...
        # Key difference between info and self.info
        print(info)

        #second method using self.info
        self.info = info
        print(self.info)
        
Student(name = "Daisy", age = 20, cgpa = 8.8, dept = "EEE")


        