# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

from functools import reduce
from operator import mul
import time
import math
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower


s = "Salem"
upper, lower = count_case(s)
print(f"Upper case letters: {upper}, Lower case letters: {lower}")