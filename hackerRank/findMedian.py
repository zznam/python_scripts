#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    arr.sort()
    i = (math.floor(len(arr)/2))
    print(arr[i])
    pass

arr = [0, 1, 2, 4, 6, 5 ,3]

findMedian(arr)