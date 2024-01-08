#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for item in range(len(matrix[row])):
                if item != len(matrix[row]) - 1:
                    last = ' '
                else:
                    last = ''
                print("{:d}".format(matrix[row][item]), end=last)
            print()
