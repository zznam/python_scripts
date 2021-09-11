#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def isPalindrome(s):
    ret = True

    startIdx = 0
    endIdx = len(s) - 1

    while (startIdx < endIdx):
        if s[startIdx] != s[endIdx]:
            ret = False
            break
        startIdx += 1
        endIdx -= 1

    return ret


def palindromeIndex(s):
    # Write your code here
    startIdx = 0
    endIdx = len(s) - 1

    while (startIdx < endIdx):
        if s[startIdx] != s[endIdx]:
            s2 = s[startIdx + 1:endIdx + 1]
            if (isPalindrome(s2)):
                return startIdx
            s3 = s[startIdx:endIdx]
            if (isPalindrome(s3)):
                return endIdx
        startIdx += 1
        endIdx -= 1

    return -1


print(palindromeIndex("aaab"))
