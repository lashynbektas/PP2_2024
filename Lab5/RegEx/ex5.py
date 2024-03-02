# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re
string = input()
l = re.compile('a.*?b$')
k = l.search(string)
if k:
    print('it\'s a match')
else:
    print('no match found')