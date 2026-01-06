class Student:
    def __new__(cls,age):
        if age < 18:
            print("Underage - cannot create object")
            return None
        return super().__new__(cls)
    
    def __init__(self,age):
        self.age = age

s1 = Student(10)
s2 = Student(21)

# We cannot print the age of s1 cause it doesn't satisfy the condition
# This is use of __new__ in the part of object creation
print(s2.age)