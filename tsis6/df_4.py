def count_lines(filename):
    """
    Counts the number of lines in a text file.
    """
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            count += 1
        print(f"The file '{filename}' has {count} lines.")

# example usage
filename = "example.txt"
count_lines(filename)
