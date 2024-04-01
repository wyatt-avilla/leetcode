# https://leetcode.com/problems/leaf-similar-trees

from __future__ import annotations

from data_structures import TreeNode


class Solution:
    def leafSimilar(self, root: [TreeNode | None], root2: [TreeNode | None]) -> bool:
        def get_lvs(root: [TreeNode | None]) -> list[int]:
            lvs: list[int] = []

            if root is None:
                return lvs
            if root.left is None and root.right is None:
                return [root.val]

            lvs += get_lvs(root.left)
            lvs += get_lvs(root.right)

            return lvs

        return get_lvs(root) == get_lvs(root2)
