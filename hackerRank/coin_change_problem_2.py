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


def getWays(n, c, index, memo):
    # Write your code here
    ways = 0
    if (index == len(c) - 1):
        if (n % c[index] == 0):
            ways += 1
        return ways
    amountWithCoin = 0
    key = str(n) + "-" + str(index)
    if (key in memo):
        return memo[key]
    while (amountWithCoin < n):
        if (index < len(c) - 1):
            remaining = n - amountWithCoin
            ways += getWays(remaining, c, index + 1, memo)
        amountWithCoin += c[index]
        if (amountWithCoin == n): ways += 1
    memo[key] = ways
    return ways


n = 3
c = [8, 3, 1, 2]
memo = {}
print(getWays(n, c, 0, memo))