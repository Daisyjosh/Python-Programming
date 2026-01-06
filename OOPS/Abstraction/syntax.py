from abc import ABC, abstractmethod

class Animal(ABC): #Abstract Class

    @abstractmethod #Abstract Methods
    def breath(self): 
        pass