#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    indexes = len(my_list) - 1
    for idx in range(indexes, -1, -1):
        print('{:d}'.format(my_list[idx]))
    if not my_list:
        pass
