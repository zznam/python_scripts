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
    ret = 0
    i = 0
    while (i < len(petrolpumps)):
        curPump = petrolpumps[i]
        petrol = curPump[0]
        curIdx = i + 1
        while (curIdx != i):

            canGoNext = petrol >= curPump[1]

            if (canGoNext):
                petrol -= curPump[1]
                if (curIdx == len(petrolpumps)):
                    curIdx = 0
                nextPump = petrolpumps[curIdx]
                curPump = nextPump
                petrol += nextPump[0]
                curIdx += 1
            else:
                break
        if (i == curIdx):
            ret = i
            break
        i += 1

    return ret


petrolpumps = [[1, 5], [10, 3], [3, 4]]

result = truckTour(petrolpumps)

print(result)
