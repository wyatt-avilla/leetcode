# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        numsLen = len(nums)
        best = 100001
        start = end = currentSum = 0
        while start < numsLen:
            if currentSum < target and end < numsLen:
                currentSum += nums[end]
                end += 1
            elif currentSum >= target:
                best = min(end - start, best)
                currentSum -= nums[start]
                start += 1
            else:
                currentSum -= nums[start]
                start += 1
        return best if best < 100001 else 0



                



cases = [
        (7, [2,3,1,2,4,3], 2),
        (4, [1,4,4], 1),
        (11, [1,1,1,1,1,1,1,1], 0),
        ]

for case in cases:
    target, nums, exp = case
    res = Solution().minSubArrayLen(target, nums)
    if res != exp:
        print(f"({target},{nums})->{res} != {exp}")
