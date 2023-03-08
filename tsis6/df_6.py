import string

def generate_files():
    """
    Generates 26 text files named A.txt, B.txt, and so on up to Z.txt.
    """
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as f:
            f.write(f"This is file {filename}.")
        print(f"File '{filename}' has been created.")

# example usage
generate_files()
