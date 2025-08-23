# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/


class Solution:
    @staticmethod
    def minimumArea(grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        min_row, max_row = rows - 1, 0
        min_col, max_col = cols - 1, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue

                min_row = min(min_row, r)
                max_row = max(max_row, r)
                min_col = min(min_col, c)
                max_col = max(max_col, c)

        return max(0, (max_row - min_row + 1) * (max_col - min_col + 1))

    @staticmethod
    def transpose(mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        return [[mat[r][c] for r in range(rows)] for c in range(cols)]

    @staticmethod
    def min_via_row_splits(grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = rows * cols

        for r_split_start in range(1, rows):
            top_unsplit = Solution.minimumArea(grid[:r_split_start])
            bot_unsplit = Solution.minimumArea(grid[r_split_start:])
            for c_split_start in range(1, cols):
                top_left = Solution.minimumArea(
                    [row[:c_split_start] for row in grid[:r_split_start]],
                )
                top_right = Solution.minimumArea(
                    [row[c_split_start:] for row in grid[:r_split_start]],
                )
                bot_left = Solution.minimumArea(
                    [row[:c_split_start] for row in grid[r_split_start:]],
                )
                bot_right = Solution.minimumArea(
                    [row[c_split_start:] for row in grid[r_split_start:]],
                )

                ans = min(
                    (
                        ans,
                        top_unsplit + bot_left + bot_right,
                        bot_unsplit + top_left + top_right,
                    ),
                )

            for r2_split_start in range(r_split_start + 1, rows):
                mid = Solution.minimumArea(grid[r_split_start:r2_split_start])
                bot = Solution.minimumArea(grid[r2_split_start:])
                ans = min(ans, top_unsplit + mid + bot)

        return ans

    def minimumSum(self, grid: list[list[int]]) -> int:
        return min(
            Solution.min_via_row_splits(grid),
            Solution.min_via_row_splits(Solution.transpose(grid)),
        )


if __name__ == "__main__":
    assert (
        Solution().minimumSum(
            [
                [1, 0, 1],
                [1, 1, 1],
            ],
        )
        == 5
    )

    assert (
        Solution().minimumSum(
            [
                [1, 0, 1, 0],
                [0, 1, 0, 1],
            ],
        )
        == 5
    )

    assert (
        Solution().minimumSum(
            [
                [1, 0, 0, 1],
                [0, 0, 0, 1],
            ],
        )
        == 3
    )

    assert (
        Solution().minimumSum(
            [
                [0, 0, 1, 1],
                [0, 0, 0, 1],
            ],
        )
        == 3
    )

    assert (
        Solution().minimumSum(
            [
                [1, 0, 0, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 1],
            ],
        )
        == 6
    )

    assert (
        Solution().minimumSum(
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 1],
                [1, 1, 0],
            ],
        )
        == 3
    )

    assert (
        Solution().minimumSum(
            [
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
            ],
        )
        == 6
    )
