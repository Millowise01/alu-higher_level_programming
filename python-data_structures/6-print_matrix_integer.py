#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for current_list in matrix:
        for num in range(len(current_list)):
            print("{:d}".format(current_list[num]), end="")
            if num != len(current_list) - 1:
                print(" ", end="")
        print()
