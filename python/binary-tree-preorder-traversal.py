# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def DFS(root: TreeNode, pathList: List):
            if root is None:
                return
            pathList.append(root.val)
            (DFS(root.left, pathList))
            (DFS(root.right, pathList))

        preorderList = []
        DFS(root, preorderList)
        return preorderList





t = TreeNode(1)
t.right = TreeNode(2, None, TreeNode(3))

print(Solution().preorderTraversal(t))
