# https://leetcode.com/problems/game-of-life/

from __future__ import annotations


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m: int = len(board)
        n: int = len(board[0])
        next_board: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                alive_neighbors: int = 0

                start_row = max(0, row - 1)
                end_row = min(m, row + 2)
                for adj_row in range(start_row, end_row):
                    start_col = max(0, col - 1)
                    end_col = min(n, col + 2)
                    for adj_col in range(start_col, end_col):
                        if board[adj_row][adj_col] == 1:
                            alive_neighbors += 1

                current_cell = board[row][col]
                if current_cell == 1:
                    alive_neighbors -= 1  # accounting for self as alive neighbor
                    if alive_neighbors < 2:
                        next_board[row][col] = 0
                    elif alive_neighbors == 2 or alive_neighbors == 3:
                        next_board[row][col] = 1
                    elif alive_neighbors > 3:
                        next_board[row][col] = 0
                elif current_cell == 0:
                    if alive_neighbors == 3:
                        next_board[row][col] = 1

        for i in range(m):
            board[i] = next_board[i]


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
for row in board:
    print(row)
print("----")
Solution().gameOfLife(board)
for row in board:
    print(row)
print("----")
