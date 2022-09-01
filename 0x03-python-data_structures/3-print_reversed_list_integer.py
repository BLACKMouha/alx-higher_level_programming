#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_my_list = len(my_list) - 1
    for idx in range(len(my_list) // 2):
        temp1 = my_list[len_my_list]
        temp2 = my_list[idx]
        my_list[idx] = temp1
        my_list[len_my_list] = temp2
        len_my_list -= 1

    for idx in range(len(my_list)):
        print('{:d}'.format(my_list[idx]))
    if not my_list:
        pass
