#!/usr/bin/python3

def remove_char_at(str, n):
    if n < len(str):
        for i in range(len(str)):
            if i != n:
                print(str[i], end='')
