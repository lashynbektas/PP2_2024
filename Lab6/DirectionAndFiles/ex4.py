# Write a Python program to count the number of lines in a text file.

import os

def count_lines(file_path):
    with open(file_path, 'r') as file:
        print("Number of lines:", len(file.readlines()))