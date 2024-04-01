# https://leetcode.com/problems/all-possible-full-binary-trees/

from __future__ import annotations

from functools import cache

from data_structures import TreeNode


class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode()]
        return_trees = []
        for i in range(1, n - 1):
            if i % 2 == 1 and (n - 1 - i) % 2 == 1:
                left_sub_trees = self.allPossibleFBT(i)
                right_sub_trees = self.allPossibleFBT(n - 1 - i)
                for left_tree in left_sub_trees:
                    for right_tree in right_sub_trees:
                        temp_root = TreeNode(0, left_tree, right_tree)
                        return_trees.append(temp_root)
        return return_trees


trees = Solution().allPossibleFBT(7)
for tree in trees:
    print("----")
    print(tree)
