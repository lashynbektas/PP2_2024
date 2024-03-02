# Write a python program to convert snake case string to camel case string.

import re
def snake_to_camel(snake_case):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_case)

snake = "hello_everyone"
camel_case = snake_to_camel(snake)

print(f"{camel_case}")