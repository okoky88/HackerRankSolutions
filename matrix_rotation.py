#!/bin/python3

import math
import os
import random
import re
import sys


# Get next index in a layer
def get_next(m, n, l, i, j):
    if i < m - 1 + l and j == l:
        i += 1
    elif i == m - 1 + l and j < n - 1 + l:
        j += 1
    elif i > l and j == n - 1 + l:
        i -= 1
    elif i == l and j > l:
        j -= 1

    return i, j


# Get indexes after n rotations
def rotate_n(m, n, l, r):
    i = l
    j = l

    for x in range(r):
        i, j = get_next(m, n, l, i, j)

    return i, j


# Complete the matrixRotation function below.
def matrixRotation(matrix, m, n, r):
    even = min(n, m)

    new_mat = [[0] * n for i in range(m)]

    for l in range(0, int(even / 2)):

        # Length of a layer 2 * rows + 2 * cols -4
        layer_len = n * 2 + m * 2 - 4
        # Full rotations is equivalent to 0
        n_rotations = r % layer_len

        # Get indexes in current matrix
        i, j = rotate_n(m, n, l, n_rotations)

        # Indexes in new matrix
        i0 = l
        j0 = l

        for x in range(layer_len):

            # Add element to new matrix
            new_mat[i][j] = matrix[i0][j0]

            # Advance indexes
            i, j = get_next(m, n, l, i, j)
            i0, j0 = get_next(m, n, l, i0, j0)

        m -= 2
        n -= 2

    for row in new_mat:
        for element in row:
            print("{0} ".format(element), end='')
        print("")


if __name__ == '__main__':
    mnr = input().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, m, n, r)
