class Student:
    @property
    def cgpa(self):
        """CGPPA of the student"""
        return 8.8
    
print(Student.cgpa.__doc__)
