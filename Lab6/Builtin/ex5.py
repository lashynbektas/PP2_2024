# Write a Python program with builtin function that returns True if all elements of the tuple are true.

from functools import reduce
from operator import mul
import time
import math
def true(elements):
    return all(elements)

print(true((True, True, True)))
print(true((True, False, True)))