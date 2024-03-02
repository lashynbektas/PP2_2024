# Write a Python program to calculate the area of a trapezoid.

import math
height = int(input("Height: "))
base = int(input("Base, first value: "))
base2 = int (input("Base, second value: "))
area = (((base+base2)/2)*height)
print("Expected Output: ", area)