#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple = ()

    if len(tuple_a) > len(tuple_b):
        idx = 0
        for i in range(len(tuple_b)):
            s = tuple_a[i] + tuple_b[i]
            sum_tuple += s,
            idx += 1
        for j in range(idx, len(tuple_a)):
            sum_tuple += tuple_a[j],

    if len(tuple_b) > len(tuple_a):
        idx = 0
        for i in range(len(tuple_a)):
            s = tuple_a[i] + tuple_b[i]
            sum_tuple += s,
            idx += 1
        for j in range(idx, len(tuple_b)):
            sum_tuple += tuple_a[j],

    if len(tuple_a) == len(tuple_b):
        for i in range(len(tuple_b)):
            s = tuple_a[i] + tuple_b[i]
            sum_tuple += s,

    return sum_tuple
