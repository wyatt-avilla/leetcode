# https://leetcode.com/problems/diagonal-traverse/

from collections.abc import Generator


class Solution:
    @staticmethod
    def diag_gen(mat: list[list[int]]) -> Generator[int, None, None]:
        max_row, max_col = len(mat) - 1, len(mat[0]) - 1
        r = c = 0
        traversing_up_right = True
        while r <= max_row and r >= 0 and c <= max_col and c >= 0:
            yield mat[r][c]
            if traversing_up_right:
                if r > 0 and c < max_col:
                    r -= 1
                    c += 1
                else:
                    traversing_up_right = False
                    if c < max_col:
                        c += 1
                    else:
                        r += 1
            else:
                if r < max_row and c > 0:
                    r += 1
                    c -= 1
                else:
                    traversing_up_right = True
                    if r < max_row:
                        r += 1
                    else:
                        c += 1

    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        return list(Solution.diag_gen(mat))


if __name__ == "__main__":
    assert Solution().findDiagonalOrder(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
    ) == [1, 2, 4, 7, 5, 3, 6, 8, 9]

    assert Solution().findDiagonalOrder(
        [
            [1, 2],
            [3, 4],
        ],
    ) == [1, 2, 3, 4]

    assert Solution().findDiagonalOrder(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
        ],
    ) == [1, 2, 4, 7, 5, 3, 6, 8, 10, 11, 9, 12]

    assert Solution().findDiagonalOrder(
        [
            [1],
            [2],
            [3],
            [4],
        ],
    ) == [1, 2, 3, 4]

    assert Solution().findDiagonalOrder(
        [
            [1, 2, 3, 4],
        ],
    ) == [1, 2, 3, 4]
