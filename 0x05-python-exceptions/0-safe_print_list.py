#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num_el_printed, i = 0, 0
        while i < x:
            print(my_list[i], end='')
            num_el_printed += 1
            i += 1
        print()
    except IndexError as err:
        print()
    return num_el_printed
