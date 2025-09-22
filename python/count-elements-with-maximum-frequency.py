# https://leetcode.com/problems/count-elements-with-maximum-frequency/

from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counts = Counter(nums)
        maxf = max(counts.values())

        return sum(v for k, v in counts.items() if v == maxf)


if __name__ == "__main__":
    assert Solution().maxFrequencyElements([1, 2, 2, 3, 1, 4]) == 4
    assert Solution().maxFrequencyElements([1, 2, 3, 4, 5]) == 5
