# Write a Python program to drop microseconds from datetime.

import datetime 
time = datetime.datetime.today().replace(microsecond=0)
print(time)