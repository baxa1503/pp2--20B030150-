def all_true(tuple_var):
    """
    Checks if all elements of a tuple are true or not.
    """
    return all(tuple_var)

# test the function
print(all_true((True, True, True)))  # True
print(all_true((True, False, True))) # False
