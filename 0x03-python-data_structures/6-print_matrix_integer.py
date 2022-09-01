#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        if sublist == []:
            print()
        for idx in range(len(sublist)):
            if idx == len(sublist) - 1:
                print("{}".format(sublist[idx]))
            if idx != len(sublist) - 1:
                print("{} ".format(sublist[idx]), end='')
