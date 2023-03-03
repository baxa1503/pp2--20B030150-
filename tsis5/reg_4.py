import re

string = input("Enter a string: ")

pattern = r'[A-Z][a-z]+'
matches = re.findall(pattern, string)

if matches:
    print("Match found:", matches)
else:
    print("No match found.")
