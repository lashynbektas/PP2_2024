# Write a Python program that invoke square root function after specific milliseconds.

from functools import reduce
from operator import mul
import time
import math
def delayed_sqrt(n, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(n)


n = 25200
delay_ms = 2123
result = delayed_sqrt(n, delay_ms)
print(f"Square root of {n} after {delay_ms} milliseconds is {result}")