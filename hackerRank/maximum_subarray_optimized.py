#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#


def getMaxSubArrEndingAtIdx(arr, i, memo):
    if (i == 0): return arr[0]
    if (i in memo):
        return memo[i]
    ret = max(arr[i], getMaxSubArrEndingAtIdx(arr, i - 1, memo) + arr[i])
    memo[i] = ret
    return ret

#Kadane's algorithm
def maxSubarray(arr):
    maxItem = arr[0]
    # maximum subarray
    ret = arr[0]
    # maximum subsequence
    ret2 = 0
    i = 0
    memo = {}
    while (i < len(arr)):
        if (arr[i] > 0):
            ret2 += arr[i]
        if (arr[i] > maxItem):
            maxItem = arr[i]
        ret = max(ret, getMaxSubArrEndingAtIdx(arr, i, memo))
        i += 1
    if (ret2 == 0):
        ret2 = maxItem
    return [ret, ret2]


result = maxSubarray([1, 2, 3, 4])
print(" ".join(map(str, result)))

result = maxSubarray([2, -1, 2, 3, 4, -5])
print(" ".join(map(str, result)))