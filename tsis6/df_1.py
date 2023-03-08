import os

def list_files(path, show_all=False, show_dirs=True, show_files=True):
    """
    Lists all files and directories in a specified path.
    """
    items = os.listdir(path)  # get a list of all items in the path
    for item in items:
        full_path = os.path.join(path, item)  # get the full path of the item
        if show_all or ((os.path.isdir(full_path) and show_dirs) or (os.path.isfile(full_path) and show_files)):
            # check if the item is a directory or a file, and if we should show it based on the arguments
            print(full_path)

# example usage
path = "/path/to/directory"
print("Directories:")
list_files(path, show_dirs=True, show_files=False)
print("Files:")
list_files(path, show_dirs=False, show_files=True)
print("All:")
list_files(path, show_all=True)
