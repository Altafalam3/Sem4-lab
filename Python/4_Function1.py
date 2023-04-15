def add_iterables(*args):
    """
    This function adds all the elements of the iterables passed as parameters.
    Parameters:
    *args: The iterables to be added.
    Returns:
    result: A list containing the sum of elements of each iterable.
    """
    result = [sum(x) for x in zip(*args)]
    return result

# Example 1
print(add_iterables([1, 2, 3], [4, 5, 6]))
# Output: [5, 7, 9]

# Example 2
print(add_iterables([1, 2, 3], [4, 5, 6], [7, 8, 9]))
# Output: [12, 15, 18]
