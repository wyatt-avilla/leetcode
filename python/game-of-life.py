# https://leetcode.com/problems/game-of-life/

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m: int = len(board)
        n: int = len(board[0])
        nextBoard: List[List[int]] = [[0 for _ in range(n)] for _ in range(m)]
        
        for row in range(m):
            for col in range(n):
                aliveNeighbors: int = 0
                
                startRow = row - 1 if row - 1 > 0 else 0
                endRow = row + 2 if row + 2 < m else m
                for adjRow in range(startRow, endRow):
                    startCol = col - 1 if col - 1 > 0 else 0
                    endCol = col + 2 if col + 2 < n else n
                    for adjCol in range(startCol, endCol):
                        if board[adjRow][adjCol] == 1:
                            aliveNeighbors += 1

                currentCell = board[row][col]
                if currentCell == 1:
                    aliveNeighbors -= 1 # accounting for self as alive neighbor
                    if aliveNeighbors < 2:
                        nextBoard[row][col] = 0
                    elif aliveNeighbors == 2 or aliveNeighbors == 3:
                        nextBoard[row][col] = 1
                    elif aliveNeighbors > 3:
                        nextBoard[row][col] = 0
                elif currentCell == 0:
                    if aliveNeighbors == 3:
                        nextBoard[row][col] = 1
        
        for i in range(m):
            board[i] = nextBoard[i]

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
for row in board:
    print(row)
print("----")
Solution().gameOfLife(board)
for row in board:
    print(row)
print("----")
