# Write a Python program to calculate the area of regular polygon.

import math

sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
apothem = length / (2 * math.tan(math.pi / sides))
area = int((sides * length * apothem) / 2)

print("The area of the polygon is:", area)