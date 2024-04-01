# https://leetcode.com/problems/longest-increasing-subsequence/

from __future__ import annotations


class Solution:
    def lengthOflis_(self, nums: list[int]) -> int:
        num_len = len(nums)
        lis_table = [0] * num_len
        for i in range(num_len):
            lis_table[i] = max(
                (lis_table[j] + 1 for j in range(i) if nums[j] < nums[i]),
                default=1,
            )

        return max(lis_table)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [1, 2, 3]
nums = [7, 7, 7, 7, 7, 7]
nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(f"lis: { Solution().lengthOflis_(nums) }")
