#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    else:
        my_list.reverse()
        for num in my_list:
            print("{:d}".format(num))
    return
