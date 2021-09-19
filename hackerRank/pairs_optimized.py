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
def binary_search(input_array, value):
    """Your code goes here."""
    
    offset = 0
    while (len(input_array) > 0):
        curLen = len(input_array)
        if (curLen == 1):
            if (input_array[0] == value):
                return offset
            return -1
        mid = int(math.floor(curLen / 2))
        if (input_array[mid] == value):
            return  offset+ mid
        if (input_array[mid] > value):
            input_array = input_array[0: mid]
        else:
            offset+= mid+1
            input_array = input_array[mid + 1: curLen]
    return -1

def pairs(k, arr):
    # Write your code here
    count = 0
    arr.sort()
    for i in arr:
        if (binary_search(arr,i-k) != -1):
            count+=1
        if (binary_search(arr,i+k) != -1):
            count+=1
    return int(count/2)


k = 2
arr = [1, 5, 3, 4, 2]

print(pairs(k, arr))