# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

from functools import cache


class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i + 2 > j:
                return 0
            if i + 2 == j:
                return values[i] * values[i + 1] * values[i + 2]

            return min(
                (values[i] * values[k] * values[j] + dp(i, k) + dp(k, j))
                for k in range(i + 1, j)
            )

        return dp(0, len(values) - 1)


if __name__ == "__main__":
    assert Solution().minScoreTriangulation([1, 2, 3]) == 6
    assert Solution().minScoreTriangulation([3, 7, 4, 5]) == 144
    assert Solution().minScoreTriangulation([1, 3, 1, 4, 1, 5]) == 13
    assert Solution().minScoreTriangulation([4, 3, 4, 3, 5]) == 132
