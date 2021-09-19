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
    count = 0
    arr.sort()
    i = 0
    while (i < len(arr)):
        j = i
        findValue = arr[i] + k
        while (arr[j] < findValue and j < len(arr) - 1):
            j += 1
            if (arr[j] == findValue):
                count += 1
                break
        i += 1
    return count


k = 2
arr = [1, 5, 3, 4, 2]

print(pairs(k, arr))