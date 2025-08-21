# https://leetcode.com/problems/count-submatrices-with-all-ones/


class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        acc = 0
        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if col == 0:
                    dp[row][col] = mat[row][col]
                else:
                    dp[row][col] = 0 if mat[row][col] == 0 else dp[row][col - 1] + 1

                curr = dp[row][col]
                for k in range(row, -1, -1):
                    curr = min(curr, dp[k][col])
                    if curr == 0:
                        break
                    acc += curr

        return acc


if __name__ == "__main__":
    assert (
        Solution().numSubmat(
            [
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 0],
            ],
        )
        == 13
    )

    assert (
        Solution().numSubmat(
            [
                [0, 1, 1, 0],
                [0, 1, 1, 1],
                [1, 1, 1, 0],
            ],
        )
        == 24
    )
