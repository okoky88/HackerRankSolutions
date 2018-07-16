#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the boardCutting function below.
def boardCutting(cost_y, cost_x):

    h_cuts = 1
    v_cuts = 1

    m = len(cost_y) + 1
    n = len(cost_x) + 1

    total_cuts = m + n

    t_cost = 0

    while h_cuts + v_cuts < total_cuts:

        mx = -1
        mx_i = 0

        my = -1
        my_i = 0

        for i in range(len(cost_x)):
            if cost_x[i] > mx:
                mx = cost_x[i]
                mx_i = i

        for i in range(len(cost_y)):
            if cost_y[i] > my:
                my = cost_y[i]
                my_i = i

        if mx > my or (mx == my and n > m):
            cost_x.pop(mx_i)
            t_cost += (mx * h_cuts)
            v_cuts += 1
        else:
            cost_y.pop(my_i)
            t_cost += (my*v_cuts)
            h_cuts += 1

    # print(t_cost % (10**9 + 7))
    return t_cost % (10**9 + 7)

if __name__ == '__main__':
    # os.environ['OUTPUT_PATH'] = "sys.stdout"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        mn = input().split()

        m = int(mn[0])

        n = int(mn[1])

        cost_y = list(map(int, input().rstrip().split()))

        cost_x = list(map(int, input().rstrip().split()))

        result = boardCutting(cost_y, cost_x)

        fptr.write(str(result) + '\n')

    fptr.close()
