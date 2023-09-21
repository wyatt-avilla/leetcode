from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        arrLen = len(height)
        maxVol = 0
        left = 0
        right = arrLen - 1
        containerLen = right - left
        while (containerLen) >= 0:
            lBarH = height[left]
            rBarH = height[right]
            containerLen = right - left
            maxVol = max(maxVol, containerLen * min(lBarH, rBarH))
            if lBarH < rBarH:
                left += 1
            elif lBarH > rBarH:
                right -= 1
            elif lBarH == rBarH:
                right -= 1


        return maxVol



cases = [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1)
        ]

for case in cases:
    inp, exp = case
    res = Solution().maxArea(inp)
    if res != exp:
        print(f"({inp}) should yield {exp}, not {res}")
