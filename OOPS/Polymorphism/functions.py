class Dog:
    def sound(self):
        print("Barks..")

class Car:
    def sound(self):
        print("Horn...")

def make_sound(obj):
    obj.sound()

make_sound(Dog())
make_sound(Car())