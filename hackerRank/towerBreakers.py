#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
# both players always play optimally.

def towerBreakers(n, m):
    # Write your code here
    if (m == 1):
        return 2
    else:
        return 1 if n % 2 == 1 else 2


print(towerBreakers(2, 2))
print(towerBreakers(1, 4))