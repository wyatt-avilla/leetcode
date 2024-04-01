# https://leetcode.com/problems/add-one-row-to-tree/

from __future__ import annotations

from data_structures import TreeNode


def splice(
    node: [TreeNode | None],
    val: int,
    target_depth: int,
    current_depth: int,
    current_side: str,
    prev_node: [TreeNode | None],
) -> None:
    if current_depth == target_depth:
        if current_side == "left":
            new_node = TreeNode(val, node)
            prev_node.left = new_node
        elif current_side == "right":
            new_node = TreeNode(val, None, node)
            prev_node.right = new_node

    if node is None:
        return

    splice(node.left, val, target_depth, current_depth + 1, "left", node)
    splice(node.right, val, target_depth, current_depth + 1, "right", node)


class Solution:
    def addOneRow(
        self,
        root: [TreeNode | None],
        val: int,
        depth: int,
    ) -> [TreeNode | None]:
        if depth == 1:
            return TreeNode(val, root)
        splice(root, val, depth, 1, "left", None)

        return root


def print_tree(node: [TreeNode | None]) -> None:
    if node is None:
        return
    print(node.val)
    print_tree(node.left)
    print_tree(node.right)


t = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))

print_tree(t)
Solution().addOneRow(t, 89, 4)
print("----")
print_tree(t)
