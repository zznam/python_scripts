#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def maxMin(k, arr):
    arr.sort()
    unfairness = 0
    i = 0
    while (i <= len(arr) - k):
        temp = arr[i + k - 1] - arr[i]
        if (i == 0):
            unfairness = temp
        elif (temp < unfairness):
            unfairness = temp
        i += 1

    return unfairness


arr = [1, 4, 7, 2]
k = 2

print(maxMin(k, arr))