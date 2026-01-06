class Animal:
    def breath(self):
        print("Animal breaths..")
    
class Dog(Animal):
    pass

class Cat(Animal):
    pass

c = Cat()
c.breath()