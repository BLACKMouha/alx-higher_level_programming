#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in zip(list(a_dictionary.keys()), list(a_dictionary.values())):
        if v == value:
            del a_dictionary[k]
    return a_dictionary
