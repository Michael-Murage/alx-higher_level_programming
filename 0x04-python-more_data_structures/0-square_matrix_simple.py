#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cloned_list = [[i ** 2 for i in row] for row in matrix]
    return cloned_list

square_matrix_simple()
