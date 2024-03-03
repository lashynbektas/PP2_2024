# Write a Python program to write a list to a file.

import os

def write_list_to_file(list_items, file_path):
    with open(file_path, 'w') as file:
        for item in list_items:
            file.write(f"{item}\n")