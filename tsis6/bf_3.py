def is_palindrome(input_string):
    """
    Checks if a string is a palindrome or not.
    """
    return input_string == input_string[::-1]

# test the function
print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False
