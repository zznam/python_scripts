#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    counter = 0
    for i in range(len(q) - 1, 0, -1):
        if q[i] != i + 1:
            if q[i - 1] == i + 1:
                counter += 1
                q[i], q[i - 1] = q[i - 1], q[i]
            elif q[i - 2] == i + 1:
                counter += 2
                q[i - 2], q[i - 1] = q[i - 1], q[i - 2]
                q[i - 1], q[i] = q[i], q[i - 1]
            else:
                print('Too chaotic')
                return
    print(counter)
    # Write your code here


if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribes(q)