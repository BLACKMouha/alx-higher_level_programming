#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list is None or number is None:
        return None
    else:
        return list(map(lambda x: x*number, list(my_list)))
