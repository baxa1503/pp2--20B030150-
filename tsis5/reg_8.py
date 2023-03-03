import re

string = input("Enter a string: ")

# Split the string at uppercase letters
split_string = re.findall('[A-Z][^A-Z]*', string)

# Print the split string
print("Split string:", split_string)
