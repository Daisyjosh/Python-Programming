class Father:
    def F_property(self):
        print("Father Property")
class Mother:
    def M_property(self):
        print("Mother Property")

class Child(Father,Mother):
    pass

c = Child()
c.M_property()
c.F_property()
