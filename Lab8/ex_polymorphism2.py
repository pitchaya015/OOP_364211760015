"""
Name: Pitchaya Musimun
ID: s364211760015
Group: MIT221
"""


# polymorphism with inheritance

from math import pi

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi*(self.radius**2)

r = Rectangle(5.0,10.0)
c = Circle(7.7)

myshape = [r,c]

for x in myshape:
    print(x.area())
