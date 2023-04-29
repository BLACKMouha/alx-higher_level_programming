#!/usr/bin/python3
'''
peak module
'''

def find_peak(list_of_integers):
    '''
    finds a peak in a list of integers
    '''
    if not list_of_integers:
        return None
    else:
        list_of_integers.sort()
        return list_of_integers[-1]
