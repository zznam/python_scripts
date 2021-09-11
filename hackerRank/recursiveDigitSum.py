#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):

    sum = 0
    for num in n:
        sum += int(num)
    sum = sum * k
    if (sum < 10):
        return sum
    return superDigit(str(sum), 1)


n = "343423423434444444444444424232342323423"
k = 4
print(superDigit(n, k))
