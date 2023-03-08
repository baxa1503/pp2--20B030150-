from functools import reduce

def multiply_list(numbers):
    return reduce((lambda x, y: x * y), numbers)

# Example usage
my_list = [2, 3, 4, 5]
result = multiply_list(my_list)
print(result) # Output: 120
