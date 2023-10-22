#!/usr/bin/python3
from shape import *

def shape_info(shape):
    print(f'Area: {shape.area()}')
    print(f'Perimeter: {shape.perimeter()}')

circle = Circle(5)
print("Circle:")
shape_info(circle)

rectangle = Rectangle(4, 6)
print("\nRectangle:")
shape_info(rectangle)
