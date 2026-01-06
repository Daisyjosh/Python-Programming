from abc import ABC, abstractmethod

class Vehicle(ABC):

    def start(self):
        print("Vehicle starting...")

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):

    def drive(self):
        print("Car driving")

c = Car()
c.start()
c.drive()
