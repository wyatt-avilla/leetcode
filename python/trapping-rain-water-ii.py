# https://leetcode.com/problems/trapping-rain-water-ii/

from collections.abc import Iterable
from heapq import heapify, heappop, heappush


class Solution:
    def trapRainWater(self, height_map: list[list[int]]) -> int:
        rows = len(height_map)
        cols = len(height_map[0])

        visited = {
            *((0, c) for c in range(cols)),
            *((rows - 1, c) for c in range(cols)),
            *((r, 0) for r in range(1, rows - 1)),
            *((r, cols - 1) for r in range(1, rows - 1)),
        }

        def adj_spots(
            row: int,
            col: int,
        ) -> Iterable[tuple[int, int]]:
            return filter(
                lambda t: t not in visited
                and t[0] in range(rows)
                and t[1] in range(cols),
                (
                    (row, col - 1),
                    (row, col + 1),
                    (row - 1, col),
                    (row + 1, col),
                ),
            )

        heap = [(height_map[r][c], r, c) for r, c in visited]
        heapify(heap)

        ans = 0
        while heap:
            h, r, c = heappop(heap)
            for sr, sc in adj_spots(r, c):
                sh = height_map[sr][sc]
                if h > sh:
                    ans += h - sh
                heappush(heap, (max(h, sh), sr, sc))
                visited.add((sr, sc))

        return ans


if __name__ == "__main__":
    assert (
        Solution().trapRainWater(
            [
                [2, 2, 2],
                [2, 1, 1],
                [2, 2, 2],
            ],
        )
        == 0
    )

    assert (
        Solution().trapRainWater(
            [
                [1, 4, 3, 1, 3, 2],
                [3, 2, 1, 3, 2, 4],
                [2, 3, 3, 2, 3, 1],
            ],
        )
        == 4
    )

    assert (
        Solution().trapRainWater(
            [
                [3, 3, 3, 3, 3],
                [3, 2, 2, 2, 3],
                [3, 2, 1, 2, 3],
                [3, 2, 2, 2, 3],
                [3, 3, 3, 3, 3],
            ],
        )
        == 10
    )
