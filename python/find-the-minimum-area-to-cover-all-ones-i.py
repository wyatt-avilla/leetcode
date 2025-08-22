# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/


class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        min_row = rows - 1
        max_row = 0
        min_col = cols - 1
        max_col = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue

                min_row = min(min_row, r)
                max_row = max(max_row, r)
                min_col = min(min_col, c)
                max_col = max(max_col, c)

        return (max_row - min_row + 1) * (max_col - min_col + 1)


if __name__ == "__main__":
    assert (
        Solution().minimumArea(
            [
                [0, 1, 0],
                [1, 0, 1],
            ],
        )
        == 6
    )

    assert (
        Solution().minimumArea(
            [
                [1, 0],
                [0, 0],
            ],
        )
        == 1
    )
