class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    @property
    def area(self):
        return self.length * self.breadth

#We never store data we compute on the fly
r = Rectangle(4,5)
print(r.area)
