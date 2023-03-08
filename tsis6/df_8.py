import os

def delete_file(path):
    """
    Deletes a file by a specified path after checking for access and existence.
    """
    # check if the file exists
    if not os.path.exists(path):
        print(f"The file '{path}' does not exist.")
        return

    # check if the file is accessible
    if not os.access(path, os.R_OK):
        print(f"You do not have permission to read the file '{path}'.")
        return
    if not os.access(path, os.W_OK):
        print(f"You do not have permission to write to the file '{path}'.")
        return
    if not os.access(path, os.X_OK):
        print(f"You do not have permission to execute the file '{path}'.")
        return

    # delete the file
    os.remove(path)
    print(f"The file '{path}' has been deleted.")

# example usage
path = "example.txt"
delete_file(path)
