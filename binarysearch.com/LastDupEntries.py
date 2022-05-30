class Solution:
    def solve(self, nums):
        memo1 = {}
        memo2 = {}
        ret = []
        for num in nums:
            if num in memo1:
                memo1[num] += 1
            else:
                memo1[num] = 1
                memo2[num] = 1
        for num in nums:
            if (memo2[num] < memo1[num] or memo1[num] == 1):
                memo2[num] += 1
                ret.append(num)
        return ret


nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]

solution = Solution()

print(solution.solve(nums))
