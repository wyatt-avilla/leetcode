# https://leetcode.com/problems/pacific-atlantic-water-flow/

from collections.abc import Iterable


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])

        touching_pacific = {
            *((0, c) for c in range(cols)),
            *((r, 0) for r in range(rows)),
        }

        touching_atlantic = {
            *((rows - 1, c) for c in range(cols)),
            *((r, cols - 1) for r in range(rows)),
        }

        visited: set[tuple[int, int]] = set()

        def valid_adj_to(r: int, c: int) -> Iterable[tuple[int, int]]:
            return (
                t
                for t in (
                    (r, c + 1),
                    (r, c - 1),
                    (r + 1, c),
                    (r - 1, c),
                )
                if t[0] in range(rows)
                and t[1] in range(cols)
                and t not in visited
                and heights[t[0]][t[1]] <= heights[r][c]
            )

        pacific_reachable_from: set[tuple[int, int]] = set()
        atlantic_reachable_from: set[tuple[int, int]] = set()

        def can_reach_pacific(pos: tuple[int, int]) -> bool:
            if pos in touching_pacific or pos in pacific_reachable_from:
                pacific_reachable_from.add(pos)
                return True

            visited.add(pos)
            res = any(can_reach_pacific(next_pos) for next_pos in valid_adj_to(*pos))
            if res:
                pacific_reachable_from.add(pos)
            visited.remove(pos)

            return res

        def can_reach_atlantic(pos: tuple[int, int]) -> bool:
            if pos in touching_atlantic or pos in atlantic_reachable_from:
                atlantic_reachable_from.add(pos)
                return True

            visited.add(pos)
            res = any(can_reach_atlantic(next_pos) for next_pos in valid_adj_to(*pos))
            if res:
                atlantic_reachable_from.add(pos)
            visited.remove(pos)

            return res

        return [
            [r, c]
            for r in range(rows)
            for c in range(cols)
            if can_reach_pacific((r, c)) and can_reach_atlantic((r, c))
        ]


if __name__ == "__main__":
    assert Solution().pacificAtlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ],
    ) == [
        [0, 4],
        [1, 3],
        [1, 4],
        [2, 2],
        [3, 0],
        [3, 1],
        [4, 0],
    ]

    assert Solution().pacificAtlantic([[1]]) == [[0, 0]]
