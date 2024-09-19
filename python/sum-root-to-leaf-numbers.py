# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
from __future__ import annotations

from data_structures import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        return self.__dfs(root, [])

    def __dfs(self, node: TreeNode, stack: list[int]) -> int:
        stack.append(node.val)

        if not node.left and not node.right:
            stack_sum = int("".join(str(n) for n in stack))
            stack.pop()
            return stack_sum

        recursion_sum = 0
        if node.left:
            recursion_sum += self.__dfs(node.left, stack)
        if node.right:
            recursion_sum += self.__dfs(node.right, stack)

        stack.pop()
        return recursion_sum


s = Solution()

t = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))

print(s.sumNumbers(t))
