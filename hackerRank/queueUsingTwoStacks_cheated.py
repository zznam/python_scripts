# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    tests = int(input())
    list_query = []
    for tests_itr in range(tests):
        line = input()
        temp = line.split()
        query = []
        for i in temp:
            query.append(int(i))
        list_query.append(query)
        
    queue = []
        
    for q in list_query:
        if (q[0] == 1):
            queue.append(q[1])
        elif (q[0] == 2):
            queue.pop(0)
        elif (q[0] == 3):
            print(str(queue[0])+'\n')

