# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

from collections import Counter


class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        freqs = Counter(num % value for num in nums)
        min_freq = min(freqs[i] for i in range(value))
        leftmost = next(i for i in range(value) if freqs[i] == min_freq)

        return min_freq * value + leftmost


if __name__ == "__main__":
    assert Solution().findSmallestInteger([3, 0, 3, 2, 4, 2, 1, 1, 0, 4], 5) == 10
    assert (
        Solution().findSmallestInteger(
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
            2,
        )
        == 15
    )
    assert Solution().findSmallestInteger([1, 3, 5, 7], 2) == 0
    assert Solution().findSmallestInteger([0, 1, 2, 3, 4], 1) == 5
    assert Solution().findSmallestInteger([1, -10, 7, 13, 6, 8], 5) == 4
    assert Solution().findSmallestInteger([1, -10, 7, 13, 6, 8], 7) == 2
