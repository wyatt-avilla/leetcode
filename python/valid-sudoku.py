# https://leetcode.com/problems/valid-sudoku/

from collections import Counter
from collections.abc import Generator, Iterable


class Solution:
    @staticmethod
    def contains_max_1_per_digit(digits_and_dots: Iterable[str]) -> bool:
        return all(
            v == 1 for v in Counter(d for d in digits_and_dots if d != ".").values()
        )

    @staticmethod
    def submat_3x3_from(
        mat: list[list[str]],
        top_left_pos: tuple[int, int],
    ) -> Generator[str, None, None]:
        size = 3
        r_offset, c_offset = top_left_pos
        for r in range(size):
            for c in range(size):
                yield mat[r + r_offset][c + c_offset]

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        board_size = 9

        rows_valid = all(
            Solution.contains_max_1_per_digit(board[r]) for r in range(board_size)
        )
        cols_valid = all(
            Solution.contains_max_1_per_digit(board[r][c] for r in range(board_size))
            for c in range(board_size)
        )

        submat_start_positions = [
            (0, 0),
            (0, 3),
            (0, 6),
            (3, 0),
            (3, 3),
            (3, 6),
            (6, 0),
            (6, 3),
            (6, 6),
        ]

        submats_valid = all(
            Solution.contains_max_1_per_digit(Solution.submat_3x3_from(board, pos))
            for pos in submat_start_positions
        )

        return rows_valid and cols_valid and submats_valid


if __name__ == "__main__":
    assert Solution().isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
    )

    assert not Solution().isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
    )
