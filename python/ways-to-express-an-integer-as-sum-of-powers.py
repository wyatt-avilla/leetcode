# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

import math
from functools import cache


class Solution:
    @cache
    @staticmethod
    def rec(num: int, x: int, i: int) -> int:
        if num == 0:
            return 1
        if num < 0 or i <= 0:
            return 0

        return Solution.rec(
            num,
            x,
            i - 1,
        ) + Solution.rec(
            num - i**x,
            x,
            i - 1,
        )

    def numberOfWays(self, n: int, x: int) -> int:
        return Solution.rec(n, x, math.ceil(n ** (1 / x))) % (10**9 + 7)


if __name__ == "__main__":
    assert Solution().numberOfWays(10, 2) == 1
    assert Solution().numberOfWays(4, 1) == 2
    assert Solution().numberOfWays(281, 1) == 879177939
