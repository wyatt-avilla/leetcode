# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

from __future__ import annotations


class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        def get_max_square(
            row_idx_start: int,
            col_idx_start: int,
            matrix: list[list[int]],
        ) -> int:
            row_size = len(matrix)
            col_size = len(matrix[0])
            side_size: int = 0
            found_zero = False

            while (
                (row_idx_start + side_size < row_size)
                and (col_idx_start + side_size < col_size)
                and not found_zero
            ):
                if matrix[row_idx_start][col_idx_start + side_size] == 1:
                    if any(
                        row[col_idx_start + side_size] == 0
                        for row in matrix[row_idx_start : row_idx_start + side_size]
                    ):
                        found_zero = True

                    if not found_zero and any(
                        element == 0
                        for element in matrix[row_idx_start + side_size][
                            col_idx_start : col_idx_start + side_size + 1
                        ]
                    ):
                        found_zero = True

                    if not found_zero:
                        side_size += 1

                else:
                    break

            return side_size

        total_squares = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    total_squares += get_max_square(row, col, matrix)

        return total_squares


print(
    Solution().countSquares(
        [[1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [0, 1, 1, 1, 1], [1, 0, 1, 1, 1]],
    ),
)
