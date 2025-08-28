# https://leetcode.com/problems/sort-matrix-by-diagonals/

import itertools
from collections.abc import Generator


class Solution:
    @staticmethod
    def gen_diag_indices_starting_from(
        pos: tuple[int, int],
        n: int,
    ) -> Generator[tuple[int, int], None, None]:
        yield from itertools.takewhile(
            lambda t: t[0] < n and t[1] < n,
            ((pos[0] + i, pos[1] + i) for i in itertools.count()),
        )

    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)

        bottom_left_view_idxs: list[list[tuple[int, int]]] = [
            list(Solution.gen_diag_indices_starting_from(pos, n))
            for pos in ((r, 0) for r in reversed(range(n)))
        ]

        top_right_view_idxs: list[list[tuple[int, int]]] = [
            list(Solution.gen_diag_indices_starting_from(pos, n))
            for pos in ((0, c) for c in range(1, n))
        ]

        for idxs in bottom_left_view_idxs:
            new_diag = sorted((grid[r][c] for r, c in idxs), reverse=True)
            for v, pos in zip(new_diag, idxs):
                r, c = pos
                grid[r][c] = v

        for idxs in top_right_view_idxs:
            new_diag = sorted((grid[r][c] for r, c in idxs))
            for v, pos in zip(new_diag, idxs):
                r, c = pos
                grid[r][c] = v

        return grid


if __name__ == "__main__":
    assert Solution().sortMatrix(
        [
            [1, 7, 3],
            [9, 8, 2],
            [4, 5, 6],
        ],
    ) == [
        [8, 2, 3],
        [9, 6, 7],
        [4, 5, 1],
    ]

    assert Solution().sortMatrix(
        [
            [0, 1],
            [1, 2],
        ],
    ) == [
        [2, 1],
        [1, 0],
    ]

    assert Solution().sortMatrix([[1]]) == [[1]]
