# With return __new__

print("WHEN IT DOESN'T RETURNS")
class Student1:
    def __new__(cls):
        print("Inside the new...")
        #if we wont return it the __init__ wont be called
    def __init__(self):
        print("Came to __init__ after returned from __new__")

d = Student1()
print()

# With Return __new__
print("WHEN IT RETURNS")
class Student2:
    def __new__(cls):
        print("Inside the __new__.. object being created...")
        return super().__new__(cls)
    
    def __init__(self):
        print("Object being created and returned hence inside the default constructor.....")

s = Student2()