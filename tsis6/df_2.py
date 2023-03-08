import os

def check_access(path):
    """
    Checks the existence, readability, writability, and executability of a specified path.
    """
    if os.path.exists(path):
        # the path exists, so check its access permissions
        if os.access(path, os.R_OK):
            print(f"{path} is readable.")
        else:
            print(f"{path} is not readable.")
        if os.access(path, os.W_OK):
            print(f"{path} is writable.")
        else:
            print(f"{path} is not writable.")
        if os.access(path, os.X_OK):
            print(f"{path} is executable.")
        else:
            print(f"{path} is not executable.")
    else:
        print(f"{path} does not exist.")

# example usage
path = "/path/to/file"
check_access(path)
