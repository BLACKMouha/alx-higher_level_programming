#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for i in my_list:
        print('{}'.format(i))

if __name__ == "__main__":
    list_int = [1, 2, 3, 4]
    print_list_integer(list_int)
