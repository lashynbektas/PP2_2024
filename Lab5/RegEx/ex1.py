# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re
string = input()
l = re.compile('ab*?')
k = l.search(string)
if k:
    print('it\'s a match')
else:
    print('no match found')