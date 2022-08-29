#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n > (len(str) - 1):
        return str

    final_str = ""
    for c in str:
        if c == str[n]:
            continue
        else:
            final_str += c
    return final_str
