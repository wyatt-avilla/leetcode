# https://leetcode.com/problems/minimum-size-subarray-sum/

from __future__ import annotations


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        nums_len = len(nums)
        best = 100001
        start = end = current_sum = 0
        while start < nums_len:
            if current_sum < target and end < nums_len:
                current_sum += nums[end]
                end += 1
            elif current_sum >= target:
                best = min(end - start, best)
                current_sum -= nums[start]
                start += 1
            else:
                current_sum -= nums[start]
                start += 1
        return best if best < 100001 else 0


cases = [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
]

for case in cases:
    target, nums, exp = case
    res = Solution().minSubArrayLen(target, nums)
    if res != exp:
        print(f"({target},{nums})->{res} != {exp}")
