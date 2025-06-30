# https://leetcode.com/problems/longest-harmonious-subsequence/

from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counts = Counter(nums)
        return max(
            max(counts.get(n - 1, -c) + c, counts.get(n + 1, -c) + c)
            for n, c in counts.items()
        )


if __name__ == "__main__":
    assert Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]) == 5
    assert Solution().findLHS([1, 2, 3, 4]) == 2
    assert Solution().findLHS([1, 1, 1, 1]) == 0
    assert Solution().findLHS([-3, -1, -1, -1, -3, -2]) == 4
