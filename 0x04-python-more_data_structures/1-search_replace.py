#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_my_list = my_list[:]
    for m in range(len(new_my_list)):
        if new_my_list[m] == search:
            new_my_list[m] = replace
    return new_my_list
