#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    copy_my_list = my_list.copy()
    copy_my_list.sort()

    return copy_my_list[len(copy_my_list) - 1]
