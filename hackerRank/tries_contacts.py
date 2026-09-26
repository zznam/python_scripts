#!/bin/python3

import math
import os
import random
import re
import sys


class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.weight = -1


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
        self.memo = {}

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key, weight):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        cursor = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not cursor.children[index]:
                cursor.children[index] = self.getNode()
            cursor = cursor.children[index]

        # mark last node as leaf
        cursor.weight = weight

    def search(self, key):

        # Search key in the trie
        # Returns weight if key presents
        # in trie, else  - 1
        cursor = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not cursor.children[index]:
                return -1
            cursor = cursor.children[index]

        return cursor.weight

    def findMaxWeightByNode(self, cursor):
        if not cursor: return -1
        max = cursor.weight
        for child in cursor.children:
            if (child):
                temp = self.findMaxWeightByNode(child)
                if (temp > max):
                    max = temp
        return max

    def findMaximumWeight(self, key):
        # the maximum possible weight of the match for given query,
        # else -1, in case no valid result is obtained.
        if (key in self.memo): return self.memo[key]
        cursor = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not cursor.children[index]:
                return -1
            cursor = cursor.children[index]
        
        ret=  self.findMaxWeightByNode(cursor)
        self.memo[key] = ret
        return ret


# nAndp = input()
# temp = nAndp.split(" ")
# n = int(temp[0])
# p = int(temp[1])

# trie = Trie()

# for i in range(n):
#     line = input()
#     temp = line.split(" ")
#     trie.insert(temp[0], int(temp[1]))

# for i in range(p):
#     key = input()
#     print(trie.findMaximumWeight(key))

nAndp = "2 1"
temp = nAndp.split(" ")
n = int(temp[0])
p = int(temp[1])

trie = Trie()

hela = ["hackerearth 10", "hackerrank 9"]
for i in range(n):
    line = hela[i]
    temp = line.split(" ")
    trie.insert(temp[0], int(temp[1]))
hela = ["hacker"]
for i in range(p):
    key = hela[i]
    print(trie.findMaximumWeight(key))
