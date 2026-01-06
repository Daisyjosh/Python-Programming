class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.gender = "Female"
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
s1 = Student("Daisy",20)
s2 = Student("Alice",20)
s1.display()
s2.display()
print(s1.gender)