# https://leetcode.com/problems/binary-tree-preorder-traversal/

from __future__ import annotations

from data_structures import TreeNode


class Solution:
    def preorderTraversal(self, root: [TreeNode | None]) -> list[int]:
        def DFS(root: TreeNode, path_list: list) -> None:
            if root is None:
                return
            path_list.append(root.val)
            DFS(root.left, path_list)
            DFS(root.right, path_list)

        preorder_list = []
        DFS(root, preorder_list)
        return preorder_list


t = TreeNode(1)
t.right = TreeNode(2, None, TreeNode(3))

print(Solution().preorderTraversal(t))
