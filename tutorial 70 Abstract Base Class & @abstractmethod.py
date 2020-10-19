# suppose we want to implement a specific rule that all classes must include
# for that we use abstractmethod

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = int(input('enter the length in meters\n'))
        self.breadth =int(input('enter the breadth in meters\n'))

    def printarea(self):
        print(f'The area of the rectangle is {self.length*self.breadth} meters')
        return ' '

rect1 = Rectangle()
print(rect1.printarea())