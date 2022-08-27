#!/usr/bin/python3

for first in range(10):
    for last in range(10):
        if first < last:
            if first != 8 and last != 9:
                print('{}{}, '.format(first, last), end='')
            if first == 8 and last == 9:
                print('{}{}'.format(first, last))
