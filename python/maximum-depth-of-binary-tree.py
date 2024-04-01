# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional
from data_structures import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode], currentLevel=0) -> int:
        if root is None:
            return currentLevel
        print(f"level {currentLevel} w/ value {root.val}")

        return max(self.maxDepth(root.left, currentLevel+1), self.maxDepth(root.right, currentLevel+1))


root = TreeNode(1,
                TreeNode(2,
                         TreeNode(4, TreeNode(8), TreeNode(9)),
                         TreeNode(5, TreeNode(10), TreeNode(11))
                         ),
                TreeNode(3,
                         TreeNode(6, TreeNode(12), TreeNode(13)),
                         TreeNode(7, TreeNode(14), TreeNode(15))
                         )
                )

print(f"depth is: {Solution().maxDepth(root)}")
