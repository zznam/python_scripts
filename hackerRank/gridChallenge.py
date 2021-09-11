#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    # Write your code here
    grid2 = []
    for s in grid:
        l = list(s)
        l.sort()
        grid2.append(l)
        print(l)

    length = len(grid2[0])
    gLength = len(grid2)
    for i in range(length):
        for j in range(gLength - 1):
            print(grid2[j][i], grid2[j + 1][i])
            if (grid2[j][i] > grid2[j + 1][i]):
                return "NO"

    return "YES"


grid = ["ebazd", "fghij", "olmkn", "pqrst", "uvwxy"]
print(gridChallenge(grid))
