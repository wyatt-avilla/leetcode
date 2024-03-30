# https://leetcode.com/problems/all-possible-full-binary-trees/

from typing import Optional
from typing import List
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

    def __str__(self):
        if self.left or self.right:
            return f"({self.val}) -> ({self.left}) ({self.right})"
        return f"{self.val}"

class Solution:
    @lru_cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
            if n % 2 == 0:
                return []
            if n == 1:
                return [TreeNode()]
            else:
                returnTrees = []
                for i in range(1, n-1):
                    if i % 2 == 1 and (n-1-i) % 2 == 1:
                        leftSubTrees = self.allPossibleFBT(i)
                        rightSubTrees = self.allPossibleFBT(n-1-i)
                        for leftTree in leftSubTrees:
                            for rightTree in rightSubTrees:
                                tempRoot = TreeNode(0, leftTree, rightTree)
                                returnTrees.append(tempRoot)
                return returnTrees




trees = (Solution().allPossibleFBT(7))
for tree in trees:
    print("----")
    print(tree)
