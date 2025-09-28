# https://leetcode.com/problems/largest-perimeter-triangle/

from bisect import bisect_left
from itertools import product


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()

        for i, j in (
            (i, j) for i, j in product(reversed(range(len(nums))), repeat=2) if i != j
        ):
            a, b = nums[i], nums[j]

            side_idx = bisect_left(nums, a + b) - 1
            while side_idx in {i, j}:
                side_idx -= 1

            if side_idx >= 0 and nums[side_idx] > abs(a - b):
                return a + b + nums[side_idx]

        return 0


if __name__ == "__main__":
    assert Solution().largestPerimeter([3, 2, 3, 4]) == 10
    assert Solution().largestPerimeter([2, 1, 2]) == 5
    assert Solution().largestPerimeter([1, 2, 1, 10]) == 0
