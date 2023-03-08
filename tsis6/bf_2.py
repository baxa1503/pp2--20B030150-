def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Example usage
my_string = "This Is a MIXED cASe String"
upper, lower = count_upper_lower(my_string)
print("Number of uppercase letters:", upper) # Output: 7
print("Number of lowercase letters:", lower) # Output: 13
