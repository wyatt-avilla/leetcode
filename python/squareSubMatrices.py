from typing import List
from functools import lru_cache

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        def getMaxSquare(rowidxStart:int, colidxStart: int, matrix: List[List[int]]) -> int:
            rowSize = len(matrix)
            colSize = len(matrix[0])
            sideSize: int = 0
            foundZero = False

            while (rowidxStart + sideSize < rowSize) and (colidxStart + sideSize < colSize) and not foundZero:
                if matrix[rowidxStart][colidxStart + sideSize] == 1:
                    if any(row[colidxStart + sideSize] == 0 for row in matrix[rowidxStart:rowidxStart + sideSize]):
                        foundZero = True

                    if any(element == 0 for element in matrix[rowidxStart + sideSize][colidxStart:colidxStart + sideSize + 1]):
                        foundZero = True

                    if not foundZero:
                        sideSize += 1

                else:
                    break


            return sideSize


        totalSquares = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    totalSquares += getMaxSquare(row, col, matrix)

        return totalSquares



print(Solution().countSquares([
  [1,0,1,0,1],
  [1,0,1,1,1],
  [0,1,1,1,1],
  [1,0,1,1,1]
]))

