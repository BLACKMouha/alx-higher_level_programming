#!/usr/bin/python3

def remove_char_at(str, n):
    if 0 < n < (len(str) - 1):
        return str

    final_str = ""
    for i in range(0, len(str), 1):
        if i == n:
            continue
        else:
            final_str += str[i]
    return str
