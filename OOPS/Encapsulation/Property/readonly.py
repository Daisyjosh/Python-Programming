class Student:
    def __init__(self,roll_no):
        self.__roll_no = roll_no
    @property
    def roll(self):
        return self.__roll_no
    
s = Student(13)
print(s.roll)

# s.roll = 14 is not possible