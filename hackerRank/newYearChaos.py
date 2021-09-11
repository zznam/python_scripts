#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    steps = 0

    i = len(q) - 1
    while (i > 0):
        # number need to be at index i
        num = i + 1
        if (q[i] == num):
            pass
        elif (q[i - 1] == num):
            q[i - 1], q[i] = q[i], q[i - 1]
            steps += 1
        elif ( i > 1 and q[i - 2] == num):
            q[i - 2], q[i - 1] = q[i - 1], q[i - 2]
            q[i - 1], q[i] = q[i], q[i - 1]
            steps += 2
        else:
            return print("Too chaotic")
        i -= 1

    print(steps)


q = [2, 1, 5, 3, 4]
# q = [2, 5, 1, 3, 4]
# q = [5, 1, 2, 3, 7, 8, 6, 4]
# q = [1, 2, 5, 3, 7, 8, 6, 4]
print(q)
minimumBribes(q)
