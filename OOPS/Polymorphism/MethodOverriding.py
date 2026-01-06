# Child can change parent's method behaviour
# RunTime Polymorphism
class Animal:
    def sound(self):
        print("Animal make sounds...")

class Dog(Animal):
    def sound(self):
        print("Dog Barks...")

d = Dog()
d.sound()