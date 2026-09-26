import numpy as np


def quicksortRecur(x, left, right):
    print(x)
    if (left >= right):
        return
    mid = (left + right) >> 1
    pivot = x[mid]
    index = partition(x, left, right, pivot)
    quicksortRecur(x, left, index - 1)
    quicksortRecur(x, index, right)
    pass


def partition(x, left, right, pivot):
    while (left <= right):
        while (x[left] < pivot):
            left += 1
        while (x[right] > pivot):
            right -= 1
        if (left <= right):
            x[left], x[right] = x[right], x[left]
            left += 1
            right -= 1

    return left


def quicksort(x):
    quicksortRecur(x, 0, len(x) - 1)
    return x


x = [2, 1, 14, 3, 5]
quicksort(x)
print(x)