#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#


def truckTour(petrolpumps):
    # Write your code here
    N =  len(petrolpumps)

    s,c = 0,0
    for i in range(N) :
        p,d =  petrolpumps[i][0], petrolpumps[i][1]
        if c+p < d :
            s = i+1
            c = 0
        else :
            c += p-d
            

    return s


petrolpumps = [[1, 5], [10, 3], [3, 4]]

result = truckTour(petrolpumps)

print(result)
