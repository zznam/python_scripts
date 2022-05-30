# ==========================================================
# // Given an array of ascending numbers which has 1 missing element. Find the missing
# ex1: [1, 3, 5, 9] => 7
# ex2: [2, 6, 8, 10, 12] => 4

# problem 1 sorted array
# problem 2 un-sorted array


def find_missing_num(a):
    n = len(a)
    l = 0
    r = n - 1
    sum = a[l] + a[r]
    missed_num  = None
    while l <= r:
        if a[l] + a[r] == sum:
            l += 1
            r -= 1
        else:
            if (a[l] - a[l-1] > a[r+1] - a[r]):
                missed_num = (a[l] + a[l-1]) // 2
            else:
                missed_num = (a[r] + a[r+1]) // 2
            break
    return missed_num

def find_missing_num_desc(a):
    n = len(a)
    l = 0
    r = n - 1
    sum = a[l] + a[r]
    missed_num  = None
    while l <= r:
        if a[l] + a[r] == sum:
            l += 1
            r -= 1
        else:
            if (a[l] - a[l-1] < a[r+1] - a[r]):
                missed_num = (a[l] + a[l-1]) // 2
            else:
                missed_num = (a[r] + a[r+1]) // 2
            break
    return missed_num


print(find_missing_num_desc([9, 5, 3, 1]))

# print(find_missing_num([1, 3, 5, 9]))
# print(find_missing_num([1, 3, 5, 9]))
# print(find_missing_num([2, 6, 8, 10, 12]))
# print(find_missing_num([1, 4, 7, 13]))
# print(find_missing_num([1, 4, 7, 13, 16]))
# print(find_missing_num([1, 3, 7]))
# print(find_missing_num([-7, -3, -1, 1, 3, 5]))
