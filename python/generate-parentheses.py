# https://leetcode.com/problems/generate-parentheses/

from typing import List
from itertools import permutations

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        validMoves = list()
        def buildTree(vaildMoves: List[str], maxPathLen: int, currentPath: List[str], stackVal: int):
            if len(currentPath) == maxPathLen:
                vaildMoves.append("".join(currentPath))
                return

            if stackVal == 0:
                buildTree(vaildMoves, maxPathLen, currentPath + ["("], stackVal + 1)
            elif stackVal == maxPathLen - len(currentPath):
                buildTree(vaildMoves, maxPathLen, currentPath + [")"], stackVal - 1)
            else:
                buildTree(vaildMoves, maxPathLen, currentPath + ["("], stackVal + 1)
                buildTree(vaildMoves, maxPathLen, currentPath + [")"], stackVal - 1)


        buildTree(validMoves, n * 2, [], 0)
        return validMoves


print(Solution().generateParenthesis(4))
