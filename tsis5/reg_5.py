import re

string = input("Enter a string: ")

pattern = r'a.*b$'
match = re.search(pattern, string)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")
