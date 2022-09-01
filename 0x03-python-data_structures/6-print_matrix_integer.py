#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        for idx in range(len(sublist)):
            if idx != 0:
                print(" ", end='')
            print("{}".format(sublist[idx]), end='')
        print()
