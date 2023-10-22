#!/usr/bin/python3
import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r * self.r)
    
    def perimeter(self):
        return math.pi * (self.r * 2)
    

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return self.height * 2 + self.width * 2
