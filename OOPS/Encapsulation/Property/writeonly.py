class Student:

    def __init__(self):
        self.__password = None
    
    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self,value):
        self.__password = value

s = Student()
s.password = "DaisyPotes"

# print(s.password) Not possible 
