import os

def check_path(path):
    """
    Checks whether a given path exists or not, and prints out the filename and directory portion of the path if it exists.
    """
    if os.path.exists(path):
        print(f"{path} exists.")
        dirname = os.path.dirname(path)
        filename = os.path.basename(path)
        print(f"Directory: {dirname}")
        print(f"Filename: {filename}")
    else:
        print(f"{path} does not exist.")

# example usage
path = "/path/to/file.txt"
check_path(path)
