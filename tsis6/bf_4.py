import time
import math

def sqrt_after_milliseconds(num, milliseconds):
    """
    Computes the square root of a number after a specified number of milliseconds.
    """
    time.sleep(milliseconds / 1000)  # wait for the specified time
    result = math.sqrt(num)  # compute the square root
    return result

# example usage
num = 25100
milliseconds = 2123

print(f"Square root of {num} after {milliseconds} milliseconds is {sqrt_after_milliseconds(num, milliseconds)}")
