# Getter => reads value
# Setter => modify value safely

class Student:

    def __init__(self,cgpa):
        self.__cgpa = cgpa
    
    def get_cgpa(self):
        return self.__cgpa

    def set_cgpa(self,value):
        if value >= 0:
            self.__cgpa = value
        else:
            print("Invalin CGPA")
s1 = Student(8.8)
print(s1.get_cgpa())

s1.set_cgpa(8.9)
print(s1.get_cgpa())


