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


def fibonacciModified(t1, t2, n, memo):
    if (n == 1): return t1
    if (n == 2): return t2
    key1 = n - 2
    key2 = n - 1
    if (key1 in memo):
        num1 = memo[key1]
    else:
        num1 = fibonacciModified(t1, t2, key1, memo)
    if (key2 in memo):
        num2 = memo[key2]
    else:
        num2 = fibonacciModified(t1, t2, key2, memo)
    ret = num1 + num2**2
    memo[n] = ret
    return ret


memo = {}
print(fibonacciModified(0, 1, 6, memo))