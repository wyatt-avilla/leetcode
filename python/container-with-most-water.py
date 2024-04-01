# https://leetcode.com/problems/container-with-most-water/

from __future__ import annotations


class Solution:
    def maxArea(self, height: list[int]) -> int:
        arr_len = len(height)
        max_vol = 0
        left = 0
        right = arr_len - 1
        container_len = right - left
        while (container_len) >= 0:
            lbar_h = height[left]
            rbar_h = height[right]
            container_len = right - left
            max_vol = max(max_vol, container_len * min(lbar_h, rbar_h))
            if lbar_h < rbar_h:
                left += 1
            elif lbar_h > rbar_h or lbar_h == rbar_h:
                right -= 1

        return max_vol


cases = [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1)]

for case in cases:
    inp, exp = case
    res = Solution().maxArea(inp)
    if res != exp:
        print(f"({inp}) should yield {exp}, not {res}")
