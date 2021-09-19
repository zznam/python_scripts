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

def isBalanced(s):
    # Write your code here
        # Write your code here
    n = -1;
    while (len(s) != n):
        n = len(s);
        s = s.replace('()', '');
        s = s.replace('[]', '');
        s = s.replace('{}', '');
    
    if (len(s) == 0):
        return "YES"
    else: 
        return "NO"

s = '{{[[(())]]}}'
s = '{[(])}'
s = '{{[}}'
s = '{(([])[])[]}'
result = isBalanced(s)
print(result)
