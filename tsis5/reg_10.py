import re

camel_case_string = input("Enter a camelCase string: ")

# Convert camel case to snake case
snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()

# Print the snake case string
print("Snake case string:", snake_case_string)
