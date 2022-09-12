#!/usr/bin/python3

"""
Write a function that computes the square value of all integers of a matrix

Prototype: def square_matrix_simple(matrix[]):

Returns a new matrix
	Same size as @matrix
	Each value should be the square of the value of the input

Initial matrix should not be modified

You are not allowd to import any module

"""

def square_matrix_simple(matrix=[]):
        return [[i**2 for i in row] for row in matrix]
