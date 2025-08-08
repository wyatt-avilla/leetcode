# https://leetcode.com/problems/soup-servings/

import math
from functools import cache


class Solution:
    @staticmethod
    @cache
    def dfs(a: int, b: int) -> float:
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1.0
        if b <= 0:
            return 0.0

        return (
            Solution.dfs(a - 4, b)
            + Solution.dfs(a - 3, b - 1)
            + Solution.dfs(a - 2, b - 2)
            + Solution.dfs(a - 1, b - 3)
        ) / 4.0

    def soupServings(self, n: int) -> float:
        m = math.ceil(n / 25)

        for i in range(1, m + 1):
            if Solution.dfs(i, i) > 1 - 1e-5:
                return 1.0
        return Solution.dfs(m, m)


if __name__ == "__main__":
    assert Solution().soupServings(50) == 0.62500
    assert Solution().soupServings(100) == 0.71875
