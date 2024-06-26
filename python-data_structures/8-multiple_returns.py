#!/usr/bin/python3


def multiple_returns(sentence):
    len_of_str = len(sentence)

    if len_of_str == 0:
        first_character = None
    else:
        first_character = sentence[0]

    return len_of_str, first_character
