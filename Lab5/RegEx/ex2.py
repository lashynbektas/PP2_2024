# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re
string = input()
l = re.compile('ab{2,3}')
k = l.search(string)
if k:
    print('it\'s a match')
else:
    print('no match found')