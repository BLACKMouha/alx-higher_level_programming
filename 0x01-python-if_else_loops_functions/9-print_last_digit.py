#!/usr/bin/python3

def print_last_digit(number):
    number_str = str(number)
    print(int(number_str[len(number_str) - 1]), end='')
    return ((int(number_str[len(number_str) - 1])))
