# https://leetcode.com/problems/leaf-similar-trees

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_lvs(root: Optional[TreeNode]) -> List[int]:
            lvs: List[int] = []

            if root is None:
                return lvs
            if root.left is None and root.right is None:
                return [root.val]

            lvs += get_lvs(root.left)
            lvs += get_lvs(root.right)

            return lvs

        return get_lvs(root) == get_lvs(root2)
