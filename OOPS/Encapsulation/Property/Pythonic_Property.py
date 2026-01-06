# Without @property
# s1.get_cgpa()
# s1.set_cgpa(8.9)

# with @propery...

class Student:
    
    def __init__(self,cgpa):
        self.__cgpa = cgpa
    
    @property
    def CGPA(self):
        return self.__cgpa

    @CGPA.setter
    def CGPA(self,value):
        if value >= 0:
            self.__cgpa = value
        else:
            print("Invalid CGPA")

s1 = Student(8.8)

print(s1.CGPA)

s1.CGPA = 8.9

print(s1.CGPA)

