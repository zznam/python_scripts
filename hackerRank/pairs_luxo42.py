#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def pairs(k, arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    i1 = 0
    i2 = 1
    cnt = 0
    while True:
        if arr[i2] - arr[i1] == k:
            i1 += 1
            i2 += 1
            cnt += 1
            #distinct numbers - so no problems
            if i1 == n or i2 == n:
                break
        elif arr[i2] - arr[i1] > k:
            i1 += 1
            if i1 == n:
                break
        else:
            i2 += 1
            if i2 == n:
                break
    return cnt


k = 2
arr = [1, 5, 3, 4, 2]

print(pairs(k, arr))