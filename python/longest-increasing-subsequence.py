# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        numLen = len(nums)
        LIStable = [0] * numLen
        for i in range(numLen):
            LIStable[i] = max((LIStable[j] + 1 for j in range(i) if nums[j] < nums[i]), default=1)

        return max(LIStable)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [1,2,3]
nums = [7,7,7,7,7,7]
nums = [1,3,6,7,9,4,10,5,6]
print(f"lis: { Solution().lengthOfLIS(nums) }")
