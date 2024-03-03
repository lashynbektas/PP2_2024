# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os
def test_path_details(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")