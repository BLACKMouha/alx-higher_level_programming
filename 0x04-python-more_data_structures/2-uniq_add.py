#!/usr/bin/python3
def uniq_add(my_list=[]):
    r = 0
    my_set = set()

    for i in my_list:
        my_set.add(i)

    for i in my_set:
        r += i
    del my_set
    return r
