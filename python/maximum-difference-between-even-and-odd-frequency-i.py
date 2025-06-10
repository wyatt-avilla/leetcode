# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)

        return max(filter(lambda x: x % 2 == 1, c.values())) - min(
            filter(lambda x: x % 2 == 0, c.values())
        )


if __name__ == "__main__":
    assert Solution().maxDifference("aaaaabbc") == 3
    assert Solution().maxDifference("abcabcab") == 1
    assert Solution().maxDifference("tzt") == -1
