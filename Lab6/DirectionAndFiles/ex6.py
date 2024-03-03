# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import os

def generate_26_files():
    for i in range(65, 91): 
        with open(f"{chr(i)}.txt", 'w') as file:
            file.write(chr(i))