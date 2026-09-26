class Solution:
    def twoSum(self, nums, target) -> list:
        memo = {}
        i = 0
        for i in range(len(nums)):
            first = nums[i]
            second = target - first
            if second in memo:
                return [i, memo[second]]
            else:
                memo[first] = i




sol = Solution()
# print(sol.twoSum([3, 2, 4], 6))
# print(sol.twoSum([0,4,3,0], 0))
print(sol.twoSum([-3, 4, 3, 90], 0))
