from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_end_here = 0

        for num in nums:
            max_end_here += num

            if max_end_here > max_so_far:
                max_so_far = max_end_here
            if max_end_here < 0:
                max_end_here = 0

        return max_so_far


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums_2 = [5, 4, -1, 7, 8]

solution = Solution()

print(solution.maxSubArray(nums))
print(solution.maxSubArray(nums_2))