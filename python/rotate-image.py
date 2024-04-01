# https://leetcode.com/problems/rotate-image/

from __future__ import annotations


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n: int = len(matrix[0])
        for row in range(n):
            for col in range(row, n - row - 1):
                prev_pixel = 0
                for i in range(4):
                    if i == 0:  # in top row
                        prev_pixel = matrix[(n - 1) - col][row]
                        matrix[row][col], prev_pixel = prev_pixel, matrix[row][col]
                    if i == 1:  # in right col
                        matrix[col][(n - 1) - row], prev_pixel = (
                            prev_pixel,
                            matrix[col][(n - 1) - row],
                        )
                    if i == 2:  # in bottom row
                        (
                            matrix[(n - 1) - row][((n - 1) - row) - (col - row)],
                            prev_pixel,
                        ) = (
                            prev_pixel,
                            matrix[(n - 1) - row][((n - 1) - row) - (col - row)],
                        )
                    if i == 3:  # in left col
                        matrix[(n - 1) - col][row], prev_pixel = (
                            prev_pixel,
                            matrix[(n - 1) - row][row],
                        )


pic1 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
pic1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(pic1)):
    print("[", end="")
    for j in range(len(pic1)):
        print(f"{pic1[i][j]:2} ", end="")
    print("]")
Solution().rotate(pic1)

print("----")
for i in range(len(pic1)):
    print("[", end="")
    for j in range(len(pic1)):
        print(f"{pic1[i][j]:2} ", end="")
    print("]")
