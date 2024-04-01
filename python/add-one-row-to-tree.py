# https://leetcode.com/problems/add-one-row-to-tree/

from data_structures import TreeNode

from typing import Optional


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def splice(node: Optional[TreeNode], val: int, targetDepth: int, currentDepth: int, currentSide: str, prevNode: Optional[TreeNode]):
            if currentDepth == targetDepth:
                if currentSide == "left":
                    newNode = TreeNode(val, node)
                    prevNode.left = newNode
                elif currentSide == "right":
                    newNode = TreeNode(val, None, node)
                    prevNode.right = newNode

            if node is None:
                return

            splice(node.left, val, targetDepth, currentDepth + 1, "left", node)
            splice(node.right, val, targetDepth, currentDepth + 1, "right", node)

        if depth == 1:
            return TreeNode(val, root)
        splice(root, val, depth, 1, "left", None)
        
        return root


def printTree(node: Optional[TreeNode]):
    if node is None:
        return
    print(node.val)
    printTree(node.left)
    printTree(node.right)

t = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))

printTree(t)
Solution().addOneRow(t, 89, 4)
print("----")
printTree(t)
