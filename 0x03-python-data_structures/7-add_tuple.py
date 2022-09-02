#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 2:
        t_a_1 = tuple_a[0]
        t_a_2 = tuple_a[1]
    elif len(tuple_a) == 1:
        t_a_1 = tuple_a[0]
        t_a_2 = 0
    else:
        t_a_1 = 0
        t_a_2 = 0

    if len(tuple_b) == 2:
        t_b_1 = tuple_b[0]
        t_b_2 = tuple_b[1]
    elif len(tuple_b) == 1:
        t_b_1 = tuple_b[0]
        t_b_2 = 0
    else:
        t_b_1 = 0
        t_b_2 = 0

    sum_tuple = (t_a_1 + t_b_1, t_a_2 + t_b_2)

    return sum_tuple
