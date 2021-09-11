#!/bin/python3


def is_palindrome(s):
    return s == s[::-1]


def solve(s):
    i, j = 0, len(s) - 1
    while (i < j) and (s[i] == s[j]):
        i += 1
        j -= 1
    if i == j:
        return 0
    temp = s[i + 1:j + 1]
    if is_palindrome(temp):
        return i
    temp = s[i:j]
    if is_palindrome(temp):
        return j
    raise AssertionError


print(solve("bbb23bbb"))