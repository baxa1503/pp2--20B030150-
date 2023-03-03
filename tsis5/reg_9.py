import re

string = input("Enter a string: ")

# Insert spaces between words starting with capital letters
new_string = re.sub(r'(?<!\s)[A-Z]', r' \g<0>', string)

# Print the new string
print("New string:", new_string)
