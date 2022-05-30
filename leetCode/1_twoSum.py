class Solution:
    def twoSum(self, nums, target) -> list:
        temp = []
        idxList = []
        size = len(nums)
        for i in range(size):
            num = nums[i]
            if num <= target:
                secondNum = target - num
                if (self.findInArr(temp, secondNum) >= 0):
                    idx = self.findInArr(temp, secondNum)
                    return [i, idxList[idx]]
                idx = self.getInsertedIdx(temp, num)
                temp.insert(idx, num)
                idxList.insert(idx, i)

    def getInsertedIdx(self, arr, val):

        low = 0
        high = len(arr)

        while (low < high):
            mid = (low + high) >> 1
            if (arr[mid] < val):
                low = mid + 1
            else:
                high = mid
        return low

    def findInArr(self, arr, val):
        low = 0
        high = len(arr)
        if (high == 0): return -1
        while (low < high):
            mid = (low + high) >> 1
            if (arr[mid] == val):
                return mid
            if (arr[mid] < val):
                low = mid + 1
            else:
                high = mid

        if low < len(arr) and arr[low] == val:
            return low
        return -1


sol = Solution()
# print(sol.twoSum([3, 2, 4], 6))
# print(sol.twoSum([0,4,3,0], 0))
print(sol.twoSum([-3, 4, 3, 90], 0))
