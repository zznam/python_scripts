# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys


class Queue2S:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if (len(self.stack2) == 0):
            while (len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        if (len(self.stack2) > 0):
            return self.stack2.pop()
        return None

    def getFront(self):
        if (len(self.stack2) == 0):
            while (len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        if (len(self.stack2) > 0):
            return self.stack2[len(self.stack2) - 1]
        return None


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

    queue = Queue2S()

    for q in list_query:
        if (q[0] == 1):
            queue.enqueue(q[1])
        elif (q[0] == 2):
            queue.dequeue()
        elif (q[0] == 3):
            print(queue.getFront() + '\n')
