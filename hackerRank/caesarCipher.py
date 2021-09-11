#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    ret = ""
    CHECK = "abcdefghijklmnopqrstuvwxyz"
    for x in s:
        try:
            idx = CHECK.index(x.lower())

            idx += k

            if (idx >= len(CHECK)):
                idx = idx % len(CHECK)

            y = CHECK[idx]
            if (x.isupper()):
                y = y.upper()
            ret += y
        except:
            ret += x
            pass
    return ret


print(caesarCipher("abc--Defghijklmnopqrstuvwxyz", 3))