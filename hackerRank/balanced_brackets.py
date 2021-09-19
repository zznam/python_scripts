#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isMatchedPair(c1, c2):
    if (c1 == '(' and c2 == ')'):
        return True
    if (c1 == '{' and c2 == '}'):
        return True
    if (c1 == '[' and c2 == ']'):
        return True
    return False


def isOpeningBracket(c1):
    if (c1 == '('):
        return True
    if (c1 == '{'):
        return True
    if (c1 == '['):
        return True
    return False


def isBalanced(s):
    stack = []
    for c in s:
        if (isOpeningBracket(c)):
            stack.append(c)
        else :
            if (len(stack) == 0): return "NO"
            last = stack.pop()
            if not isMatchedPair(last, c):
                return "NO"
    if (len(stack) == 0):
        return "YES"
    return "NO"

s = '{{[[(())]]}}'
s = '{[(])}'
s = '{{[}}'
s = '{(([])[])[]}'
result = isBalanced(s)
print(result)
