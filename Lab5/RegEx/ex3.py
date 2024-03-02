# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
string = input()
l = re.compile('[a-z]+_[a-z]+')
k = l.search(string)
if k:
    print('it\'s a match')
else:
    print('no match found')