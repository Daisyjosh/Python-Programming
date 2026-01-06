class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("Daisy")
print(s1.name) # Everything is public until we protect it!!!!