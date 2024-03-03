# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted.")
    else:
        print("File does not exist or is not accessible.")