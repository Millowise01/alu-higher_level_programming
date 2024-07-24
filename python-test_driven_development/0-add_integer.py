#!/usr/bin/python3
'''
This module contains a function that adds two integers
'''

def add_integer(a, b=98):
    """Adds two integers
    Args:
        a (int): first integer
        b (int, optional): second integer Defaults to 98.
    Returns:
        int: sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
