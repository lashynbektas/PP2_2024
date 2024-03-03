# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

from functools import reduce
from operator import mul
import time
import math
def ispolindrome(a):
    return a == "".join(reversed(a))

print(ispolindrome("level"))
print(ispolindrome("moon"))