def write_list_to_file(filename, lst):
    """
    Writes a list to a file.
    """
    with open(filename, 'w') as f:
        for item in lst:
            f.write(f"{item}\n")
    print(f"The list has been written to the file '{filename}'.")

# example usage
filename = "example.txt"
lst = ["apple", "banana", "orange"]
write_list_to_file(filename, lst)
