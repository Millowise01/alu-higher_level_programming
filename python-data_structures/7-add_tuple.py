#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    len_t_a = len(list_a)
    len_t_b = len(list_b)

    if not list_a:
        list_a.extend([0, 0])
    elif len_t_a == 1:
        list_a.append(0)
    else:
        pass

    if not list_b:
        list_b.extend([0, 0])
    elif len_t_b == 1:
        list_b.append(0)
    else:
        pass

    first_item = list_a[0] + list_b[0]
    second_item = list_a[1] + list_b[1]

    returning_tuple = (first_item, second_item)

    return returning_tuple
