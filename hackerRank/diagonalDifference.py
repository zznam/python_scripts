def diagonalDifference(arr):
    # Write your code here
    ltrDiagonal = 0
    rtLDiagonal = 0
    dimensional = len(arr)
    idx1 = 0
    idx2 = dimensional - 1
    while (idx1 < dimensional):
        ltrDiagonal += arr[idx1][idx1]
        rtLDiagonal += arr[idx1][idx2]
        idx1 += 1
        idx2 -= 1

    return abs(rtLDiagonal - ltrDiagonal)


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

print(diagonalDifference(arr))