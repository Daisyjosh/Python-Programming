class Student:
    def __init__(self,*data): # Data packs values into tuples.
        print("Student data: ", data)
s1 = Student("Daisy")
s2 = Student("Daisy",20)
s3 = Student("Daisy",20,"EEE",8.8)


        