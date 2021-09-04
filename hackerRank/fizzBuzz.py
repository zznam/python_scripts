#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    arr = range(1,n +1)
    for i in arr:
        if (i%3 == 0):
            if (i%5== 0):
                print("FizzBuzz")
            else:
                print("Fizz")
            continue
        if (i % 5 == 0):
            print("Buzz")
            continue
        print(i)
            

