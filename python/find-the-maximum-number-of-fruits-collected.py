# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

from math import inf


class Solution:
    @staticmethod
    def transpose(mat: list[list[int]]) -> None:
        n = len(mat)
        for i in range(n):
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    @staticmethod
    def dp(fruits: list[list[int]], n: int) -> int:
        prev = [-inf] * n
        curr = [-inf] * n
        prev[n - 1] = fruits[0][n - 1]

        for i in range(1, n - 1):
            for j in range(max(n - 1 - i, i + 1), n):
                best = prev[j]
                if j - 1 >= 0:
                    best = max(best, prev[j - 1])
                if j + 1 < n:
                    best = max(best, prev[j + 1])
                curr[j] = best + fruits[i][j]
            prev, curr = curr, prev

        return int(prev[n - 1])

    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        n = len(fruits)
        diag_sum = sum(fruits[i][i] for i in range(n))
        upper_triangular_sum = Solution().dp(fruits, n)
        Solution().transpose(fruits)
        lower_triangular_sum = Solution().dp(fruits, n)

        return diag_sum + upper_triangular_sum + lower_triangular_sum


if __name__ == "__main__":
    assert (
        Solution().maxCollectedFruits(
            [
                [1, 2, 3, 4],
                [5, 6, 8, 7],
                [9, 10, 11, 12],
                [13, 14, 15, 16],
            ],
        )
        == 100
    )

    assert (
        Solution().maxCollectedFruits(
            [
                [1, 1],
                [1, 1],
            ],
        )
        == 4
    )

    assert (
        Solution().maxCollectedFruits(
            [
                [14, 14, 15, 16, 17, 20],
                [13, 15, 15, 16, 20, 22],
                [14, 14, 16, 16, 19, 23],
                [14, 14, 15, 21, 23, 23],
                [13, 15, 17, 18, 18, 22],
                [13, 14, 15, 18, 18, 18],
            ],
        )
        == 293
    )
