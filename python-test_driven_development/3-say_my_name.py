#!/usr/bin/python3
"""
This module contains a function that prints My name is <first name> <last name>
"""
def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>
    Args:
        first_name (str): first name
        last_name (str, optional): last name Defaults to "".
    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
