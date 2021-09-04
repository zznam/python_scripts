#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    # Write your code here
    a.sort()
    i = 0
    len2 = len(a)
    while i < len2:
        if (i == len2 - 1):
            return a[i]
        if (a[i] != a[i - 1] and a[i] != a[i + 1]):
            return a[i]
        i += 2


a = [0, 0, 1, 2, 1]

print(lonelyinteger(a))