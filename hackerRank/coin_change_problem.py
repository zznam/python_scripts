#!/bin/python3

import math
import os
import random
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#


def getWays(n, c):
    # Write your code here
    ways = 0
    i = 0
    t = c[0]
    if (len(c) == 1):
        if (n % t == 0):
            ways += 1
        return ways
    while (t * i < n):
        cLeft = c[1:len(c)]
        if (len(cLeft) > 0):
            ways += getWays(n - t * i, cLeft)
        i += 1
        if (t * i == n): ways += 1

    return ways


n = 3
c = [8, 3, 1, 2]
print(getWays(n, c))