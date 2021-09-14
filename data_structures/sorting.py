import math


def bubbleSort(arr):
    """Your code goes here."""
    lastIdx = len(arr) - 1
    while (lastIdx > 0):
        for i in range(lastIdx):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        lastIdx -= 1
    return arr


# test_list = [1, 3, 9, 11, 15, 19, 29]
# test_list = [1, 19, 9, 20, 15, 3]
# print(bubbleSort(test_list))
"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    size = len(array)
    if size == 1:
        return array
    if size == 2:
        if (array[0] > array[1]):
            array.reverse()
        return array
    pivotIdx = size - 1
    pivot = array[size - 1]
    for i in range(size):
        if (i >= pivotIdx):
            break
        while (array[i] > pivot and i < pivotIdx - 1):
            array[i], array[pivotIdx - 1], array[pivotIdx] = array[
                pivotIdx - 1], array[pivotIdx], array[i]
            pivotIdx -= 1
            # print(array)
        if (array[i] > array[pivotIdx]):
            array[i], array[pivotIdx] = array[pivotIdx], array[i]
            pivotIdx -= 1
    # print(array)
    if (pivotIdx == 0):
        left = [pivot]
    else:
        left = quicksort(array[0:pivotIdx])
        left.append(pivot)
    if (pivotIdx == size - 1):
        right = []
    else:
        right = quicksort(array[pivotIdx + 1:size])
    return left + right


test = [21, 4, 1, 3, 29, 20, 25, 6, 21, 14]
print("before", test)
print("after ", quicksort(test))
