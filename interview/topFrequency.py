import numpy as np
import datetime

''' Given an integer array nums and an integer k
write a function that returns the k most frequent elements.'''


class TopFrequency:
    def topFrequent(self, nums, k):
        length = len(nums)
        if (length == 0 or length <= k): return nums

        #let's create a dict to save frequency of each number
        memo = {}
        for num in nums:
            if (num in memo):
                memo[num] += 1
            else:
                memo[num] = 1

        # an sorted array to save k most frequent elements in term of tuple (num, frequency)
        temp = []
        for key in memo:
            value = memo[key]
            if (len(temp) < k):
                idx = self.getInsertedIdx(temp, value)
                temp.insert(idx, (key, value))
            else:
                if (value > temp[0][1]):
                    temp.pop(0)
                    idx = self.getInsertedIdx(temp, value)
                    temp.insert(idx, (key, value))

        # normalize our return array
        ret = []
        for i in temp:
            ret.append(i[0])
        return ret

    def getInsertedIdx(self, arr, val):
        #Parameters:
        #    arr (array): sorted array of 2-tuple, used second value for comparison.
        #    example arr = [(2, 3), (3, 4), (4, 5), (1, 9)] , val = 6
        #Returns:
        #    inserted index for new element with value = val
        #    return for example: 3
        low = 0
        high = len(arr)

        while (low < high):
            mid = (low + high) >> 1
            if (arr[mid][1] < val):
                low = mid + 1
            else:
                high = mid
        return low


fre = TopFrequency()
print(datetime.datetime.now())
print(fre.topFrequent([1, 1, 1, 2, 2, 3], 2))
print(fre.topFrequent([1], 1))
print(fre.topFrequent([5, 1, 1, 1, 2, 2, 3, 3, 4], 3))
print(datetime.datetime.now())

arr = np.random.randint(100 * 1000, size=10 * 1000 * 1000)
print(fre.topFrequent(arr, 7))
print(datetime.datetime.now())