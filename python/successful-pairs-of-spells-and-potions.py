# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

from bisect import bisect_left
from math import ceil


class Solution:
    def successfulPairs(
        self,
        spells: list[int],
        potions: list[int],
        success: int,
    ) -> list[int]:
        ans = [0 for _ in range(len(spells))]

        m = len(potions)
        sorted_potions = sorted((p, i) for i, p in enumerate(potions))

        for i, s in enumerate(spells):
            min_potion_strength = ceil(success / s)
            ans[i] = m - bisect_left(sorted_potions, (min_potion_strength, 0))

        return ans


if __name__ == "__main__":
    assert Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7) == [4, 0, 3]
    assert Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16) == [2, 0, 2]
