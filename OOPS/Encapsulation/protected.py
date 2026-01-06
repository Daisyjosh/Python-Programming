# prefix with single underscore refers protected members
class Student:
    def __init(self):
        self._cgpa = 8.8
s = Student()
print(s._cgpa)