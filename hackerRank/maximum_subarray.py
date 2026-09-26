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


def getSumFromIdxToIdx(arr, i, j, memo):
    if (i == j): return arr[i]
    key = str(i) + "-" + str(j)
    if (key in memo):
        return memo[key]
    ret =  arr[i] + getSumFromIdxToIdx(arr, i + 1, j, memo)
    memo[key] = ret
    return ret


def maxSubarray(arr, i, j, memo):
    ret = arr[i]
    if (i == j):
        return ret

    #all subarray contain element ith
    temp = i
    while (temp <= j):
        sum = getSumFromIdxToIdx(arr, i, temp, memo)
        ret = max(ret, sum)
        temp += 1
    ret = max(ret, maxSubarray(arr, i + 1, j, memo))
    return ret



def maxTwoSub(arr, memo):
    # Write your code here
    maxSubSeq = 0
    max = arr[0]
    for i in arr:
        if (i > 0):
            maxSubSeq += i
        if (i > max):
            max = i
    if (maxSubSeq == 0):
        maxSubSeq = max
    max1 = maxSubarray(arr, 0, len(arr) - 1, memo)
    return [max1, maxSubSeq]


memo = {}
result = maxTwoSub([1, 2, 3, 4], memo)
print(" ".join(map(str, result)))

memo = {}
result = maxTwoSub([-2, -3, -1, -4, -6], memo)
print(" ".join(map(str, result)))