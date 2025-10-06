# https://leetcode.com/problems/swim-in-rising-water/

from collections import deque


class Solution:
    @staticmethod
    def bfs(grid: list[list[int]], n: int, water_level: int) -> bool:
        seen = set()
        q = deque([(0, 0)])

        while q:
            pos = q.popleft()
            if pos == (n - 1, n - 1):
                return True

            if pos in seen:
                continue
            seen.add(pos)

            r, c = pos
            q.extend(
                t
                for t in (
                    (r, c - 1),
                    (r, c + 1),
                    (r - 1, c),
                    (r + 1, c),
                )
                if t[0] in range(n)
                and t[1] in range(n)
                and grid[t[0]][t[1]] <= water_level
                and t not in seen
            )

        return False

    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        lo = max(grid[0][0], min(grid[r][c] for r in range(n) for c in range(n)))
        hi = max(grid[r][c] for r in range(n) for c in range(n))

        while hi - lo > 0:
            mid = lo + (hi - lo) // 2
            if Solution.bfs(grid, n, mid):
                hi = mid
            else:
                lo = mid + 1

        return hi


if __name__ == "__main__":
    assert (
        Solution().swimInWater(
            [
                [3, 2],
                [0, 1],
            ],
        )
        == 3
    )
    assert (
        Solution().swimInWater(
            [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ],
        )
        == 16
    )
    assert (
        Solution().swimInWater(
            [
                [0, 2],
                [1, 3],
            ],
        )
        == 3
    )
    assert (
        Solution().swimInWater(
            [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 17],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ],
        )
        == 17
    )
    assert (
        Solution().swimInWater(
            [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 18],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ],
        )
        == 18
    )
