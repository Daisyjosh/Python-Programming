#syntax @name.deleter

class Student:
    def __init__(self,name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name

    @name.deleter
    def name(self):
        print("Name deleted")
        del self.__name


s = Student("Daisy")
del s.name