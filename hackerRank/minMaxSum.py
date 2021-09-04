#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    maxSum = 0
    minSum = 0
    sum = 0
    min = arr[0]
    max = arr[0]
    for i in arr:
        if (i < min):
            min = i
        elif (i > max):
            max = i
        sum += i

    maxSum = sum - min
    minSum = sum - max
    print(minSum, maxSum)
    pass


arr = [1, 3, 5, 7, 9]

miniMaxSum(arr)
