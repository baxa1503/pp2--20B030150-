import re

string = input("Enter a string: ")

pattern = r'a{1}b{2,3}'
matches = re.findall(pattern, string)

if matches:
    print("Match found:", matches)
else:
    print("No match found.")
