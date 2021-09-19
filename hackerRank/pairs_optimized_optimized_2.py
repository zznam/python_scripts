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
    my_dict = {}
    for i in arr:
        my_dict[i] = 1
    for i in arr:
        if (i + k in my_dict):
            count += 1

    return count


k = 2
arr = [1, 5, 3, 4, 2]

print(pairs(k, arr))