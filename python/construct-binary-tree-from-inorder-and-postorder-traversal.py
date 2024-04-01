# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from enum import Enum
from typing import List, Optional
from data_structures import TreeNode

class TraversalType(Enum):
    INORDER = 1
    POSTORDER = 2

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 or len(postorder) == 0:
            return None

        root: TreeNode = TreeNode(postorder[-1])
        root_idx: int = inorder.index(postorder[-1])

        left_subtree_inorder: List[int] = inorder[:root_idx]
        right_subtree_inorder: List[int] = inorder[root_idx + 1 :]

        postorder.pop()

        left_subtree_postorder: List[int] = postorder[: len(left_subtree_inorder)]
        right_subtree_postorder: List[int] = postorder[-len(right_subtree_inorder) :]

        root.left = self.buildTree(left_subtree_inorder, left_subtree_postorder)
        root.right = self.buildTree(right_subtree_inorder, right_subtree_postorder)

        return root


def tree_bfs_vals(root: Optional[TreeNode]) -> List[Optional[int]]:
    nodes: List[Optional[TreeNode]] = [root]
    node_vals: List[Optional[int]] = []
    for node in nodes:
        if node:
            node_vals.append(node.val)
            nodes.append(node.left)
            nodes.append(node.right)
        else:
            node_vals.append(None)

    return node_vals


def tree_order_vals(root: Optional[TreeNode], traversal: TraversalType) -> List[int]:
    order: List[int] = []

    if root is None:
        return order

    order += tree_order_vals(root.left, traversal)
    if traversal == TraversalType.INORDER:
        order.append(root.val)
    order += tree_order_vals(root.right, traversal)
    if traversal == TraversalType.POSTORDER:
        order.append(root.val)

    return order


ex1_tree = TreeNode(3)
ex1_tree.left = TreeNode(9)
ex1_tree.right = TreeNode(20)
ex1_tree.right.left = TreeNode(15)
ex1_tree.right.right = TreeNode(7)
print(tree_bfs_vals(ex1_tree))
print(tree_bfs_vals(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])))
print("--------------")

ex2_tree = TreeNode(3)
ex2_tree.left = TreeNode(9)
ex2_tree.right = TreeNode(20)
ex2_tree.left.left = TreeNode(15)
ex2_tree.left.right = TreeNode(7)
ex2_inorder = tree_order_vals(ex2_tree, TraversalType.INORDER)
ex2_postorder = tree_order_vals(ex2_tree, TraversalType.POSTORDER)
print(tree_bfs_vals(ex2_tree))
print(tree_bfs_vals(Solution().buildTree(ex2_inorder, ex2_postorder)))
print("--------------")

ex3_tree = TreeNode(1)
ex3_tree.left = TreeNode(2)
ex3_inorder = tree_order_vals(ex3_tree, TraversalType.INORDER)
ex3_postorder = tree_order_vals(ex3_tree, TraversalType.POSTORDER)
print(tree_bfs_vals(ex3_tree))
print(tree_bfs_vals(Solution().buildTree(ex3_inorder, ex3_postorder)))
print("--------------")
