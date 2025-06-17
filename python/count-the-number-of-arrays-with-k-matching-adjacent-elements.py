# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

from math import comb


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return m * comb(n - 1, k) * (m - 1) ** (n - k - 1) % (10**9 + 7)


if __name__ == "__main__":
    assert Solution().countGoodArrays(4, 2, 2) == 6
    assert Solution().countGoodArrays(5, 2, 0) == 2
    assert Solution().countGoodArrays(3, 2, 1) == 4
