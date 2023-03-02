from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def volume(self):
        pass
        
class Sphere(Shape):
    def __init__(self,a):
        self.a=a

    def volume(self):
        vol=4/3*3.14*((self.a)**3)
        print(f"Volume of Sphere is {vol}")

class Cube(Shape):
    def __init__(self,a):
        self.a=a

    def volume(self):
        vol=(self.a)**3
        print(f"Volume of Cube is {vol}")
