#!/usr/bin/python3
'''
this module contains a function that prints a square with the character #
'''
def print_square(size):
    """Prints a square with the character #
    Args:
        size (int): size length of the square
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: size must be an integer
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
