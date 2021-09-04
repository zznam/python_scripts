#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    countPos = 0
    countNeg = 0
    countZero = 0
    for i in arr:
        if (i > 0):
            countPos += 1
        elif (i < 0):
            countNeg += 1
        else:
            countZero += 1
    print("{:.6f}".format(countPos/len(arr)))
    print("{:.6f}".format(countNeg/len(arr)))
    print("{:.6f}".format(countZero/len(arr)))


arr = [1, 1, 0, -1, -1]

plusMinus(arr)
