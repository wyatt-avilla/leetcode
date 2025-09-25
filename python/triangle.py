# https://leetcode.com/problems/triangle/
from __future__ import annotations

from functools import cache


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        @cache
        def dfs(row_idx: int, col_idx: int) -> int | None:
            if row_idx >= len(triangle):
                return 0
            if col_idx >= len(triangle[row_idx]):
                return None

            left = dfs(row_idx + 1, col_idx)
            right = dfs(row_idx + 1, col_idx + 1)
            return triangle[row_idx][col_idx] + (
                min(filter(lambda x: x is not None, (left, right)))
            )

        ans = dfs(0, 0)
        assert ans is not None
        return ans


if __name__ == "__main__":
    assert Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert Solution().minimumTotal([[-10]]) == -10
