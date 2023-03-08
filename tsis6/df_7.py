def copy_file(src_file, dest_file):
    """
    Copies the contents of a file to another file.
    """
    with open(src_file, 'r') as f1, open(dest_file, 'w') as f2:
        for line in f1:
            f2.write(line)
    print(f"The contents of '{src_file}' have been copied to '{dest_file}'.")

# example usage
src_file = "source.txt"
dest_file = "destination.txt"
copy_file(src_file, dest_file)
