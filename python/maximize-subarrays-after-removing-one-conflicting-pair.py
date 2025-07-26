# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/


import math
from collections import defaultdict


class Solution:
    def maxSubarrays(self, n: int, conflicting_pairs: list[list[int]]) -> int:
        bmin1: dict[int, int | float] = defaultdict(lambda: math.inf)
        bmin2: dict[int, int | float] = defaultdict(lambda: math.inf)

        for a, b in ((min(p), max(p)) for p in conflicting_pairs):
            if bmin1[a] > b:
                bmin2[a] = bmin1[a]
                bmin1[a] = b
            elif bmin2[a] > b:
                bmin2[a] = b

        res: int | float = 0
        ib1 = n
        b2: int | float = 0x3FFFFFFF  # lol
        delcount: dict[int, int | float] = defaultdict(int)

        for i in range(n, 0, -1):
            if bmin1[ib1] > bmin1[i]:
                b2 = min(b2, bmin1[ib1])
                ib1 = i
            else:
                b2 = min(b2, bmin1[i])
            res += min(bmin1[ib1], n + 1) - i
            delcount[ib1] += min(b2, bmin2[ib1], n + 1) - min(bmin1[ib1], n + 1)

        return int(res + max(delcount.values()))


if __name__ == "__main__":
    assert Solution().maxSubarrays(4, [[2, 3], [1, 4]]) == 9
    assert Solution().maxSubarrays(5, [[1, 2], [2, 5], [3, 5]]) == 12
    assert Solution().maxSubarrays(4, [[1, 2]]) == 10
