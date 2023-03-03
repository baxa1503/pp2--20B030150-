snake_case_string = input("Enter a snake_case_string: ")

# Split the string into words
words = snake_case_string.split('_')

# Convert the first word to lowercase and the rest to uppercase
camel_case_words = [words[0].lower()] + [word.title() for word in words[1:]]

# Join the words to form a camel case string
camel_case_string = ''.join(camel_case_words)

print("Camel case string:", camel_case_string)
