# Write a Python program to list only directories, files and all directories, files in a specified path.

import os

def list_dir_files(path):
    items = os.listdir(path)
    dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in items if os.path.isfile(os.path.join(path, item))]

    print("Directories:", dirs)
    print("Files:", files)
    print("All items:", items)