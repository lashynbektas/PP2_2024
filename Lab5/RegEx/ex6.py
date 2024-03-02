# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

def replace_with_colon(content):
    result_string = content.replace(' ', ':').replace(',', ':').replace('.', ':')
    return result_string


text = 'Hello World. I am Lashyn.'
print(replace_with_colon(text))