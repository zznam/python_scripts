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
    # for i in range(0, len(arr) - k+1):
    #     print(i)
    return (min(arr[i + k - 1] - arr[i] for i in range(0, len(arr) - k + 1)))


arr = [1, 4, 7, 2]
arr = [1, 4, 7, 8]
k = 2

print(maxMin(k, arr))