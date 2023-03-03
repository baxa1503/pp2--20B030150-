import re

string = input("Enter a string: ")

pattern = r'[ ,.]'
replacement = ':'
new_string = re.sub(pattern, replacement, string)

print("New string:", new_string)
