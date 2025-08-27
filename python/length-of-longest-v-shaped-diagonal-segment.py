# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

from __future__ import annotations

import itertools
from functools import cache


class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(
            cx: int,
            cy: int,
            direction: int,
            target: int,
            *,
            can_turn: bool,
        ) -> int:
            nx, ny = cx + dirs[direction][0], cy + dirs[direction][1]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != target:
                return 0
            max_step = dfs(nx, ny, direction, 2 - target, can_turn=can_turn)
            if can_turn:
                max_step = max(
                    max_step,
                    dfs(nx, ny, (direction + 1) % 4, 2 - target, can_turn=False),
                )
            return max_step + 1

        one_positions = itertools.chain.from_iterable(
            (
                ((row_idx, col_idx) for col_idx, val in enumerate(col) if val == 1)
                for row_idx, col in enumerate(grid)
            ),
        )

        return max(
            itertools.chain.from_iterable(
                (dfs(r, c, d, 2, can_turn=True) + 1 for d in (0, 1, 2, 3))
                for r, c in one_positions
            ),
            default=0,
        )


if __name__ == "__main__":
    assert (
        Solution().lenOfVDiagonal(
            [
                [2, 2, 0, 2, 0, 2, 0],
                [1, 2, 2, 1, 0, 2, 0],
            ],
        )
        == 2
    )

    assert (
        Solution().lenOfVDiagonal(
            [
                [2, 2, 1, 2, 2],
                [2, 0, 2, 2, 0],
                [2, 0, 1, 1, 0],
                [1, 0, 2, 2, 2],
                [2, 0, 0, 2, 2],
            ],
        )
        == 5
    )

    assert (
        Solution().lenOfVDiagonal(
            [
                [2, 2, 2, 2, 2],
                [2, 0, 2, 2, 0],
                [2, 0, 1, 1, 0],
                [1, 0, 2, 2, 2],
                [2, 0, 0, 2, 2],
            ],
        )
        == 4
    )

    assert (
        Solution().lenOfVDiagonal(
            [
                [1, 1, 1, 2, 0, 0],
                [0, 0, 0, 0, 1, 2],
            ],
        )
        == 2
    )

    assert (
        Solution().lenOfVDiagonal(
            [
                [1, 2, 2],
                [1, 0, 2],
            ],
        )
        == 2
    )

    assert (
        Solution().lenOfVDiagonal(
            [
                [1, 2, 2, 2, 2],
                [2, 2, 2, 2, 0],
                [2, 0, 0, 0, 0],
                [0, 0, 2, 2, 2],
                [2, 0, 0, 2, 0],
            ],
        )
        == 5
    )

    assert Solution().lenOfVDiagonal([[1]]) == 1

    assert Solution().lenOfVDiagonal([[0]]) == 0
