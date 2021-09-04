import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    arr = s.split(":")
    if (arr[0] == "12"):
        if (arr[2].find("AM") >= 0):
            arr[0] = "00"
    else:
        if (arr[2].find("PM") >= 0):
            num = int(arr[0]) + 12
            arr[0] = str(num)
    arr[2] = arr[2][0:2]

    print(":".join(arr))
    pass

s = "07:05:45PM"
timeConversion(s)