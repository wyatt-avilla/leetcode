# https://leetcode.com/problems/symmetric-tree/

from __future__ import annotations
from data_structures import TreeNode


def compare_tree(l_node: [TreeNode | None], r_node: [TreeNode | None]) -> bool:
    if l_node is None and r_node is None:
        return True
    if l_node is None or r_node is None:
        return False

    return (
        l_node.val == r_node.val
        and compare_tree(l_node.left, r_node.right)
        and compare_tree(l_node.right, r_node.left)
    )


class Solution:
    def isSymmetric(self, root: [TreeNode | None]) -> bool:
        return compare_tree(root.left, root.right)


case1 = TreeNode(1)
case1.left = TreeNode(2)
case1.right = TreeNode(2)
case1.left.left = TreeNode(3)
case1.left.right = TreeNode(4)
case1.right.left = TreeNode(4)
case1.right.right = TreeNode(3)

assert Solution().isSymmetric(case1)
print("-----")


case2 = TreeNode(1)
case2.left = TreeNode(2)
case2.right = TreeNode(2)
case2.left.right = TreeNode(2)
case2.right.right = TreeNode(3)

assert not Solution().isSymmetric(case2)
print("-----")

case3 = TreeNode(3)
assert Solution().isSymmetric(case3)
print("-----")

case4 = TreeNode(3)
case4.left = TreeNode(0)
assert not Solution().isSymmetric(case4)

case5 = TreeNode(1)
case5.left = TreeNode(2)
case5.left.right = TreeNode(3)
case5.right = TreeNode(2)
case5.right.left = TreeNode(3)
assert Solution().isSymmetric(case5)
