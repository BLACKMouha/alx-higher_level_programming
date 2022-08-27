#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if 64 < ord(c) < 91 or c == ' ':
            print(c, end='')
        else:
            print(chr(ord(c) - 32), end='')
    print()
