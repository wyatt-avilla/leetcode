from __future__ import annotations

from data_structures import TreeNode


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        if not root:
            return ""

        return (
            str(root.val) + " " + self.serialize(root.left) + self.serialize(root.right)
        )

    def __first_gt_idx(self, val: int, nums: list[int]) -> int:
        for i, n in enumerate(nums):
            if n > val:
                return i + 1

        return len(nums) + 1

    def __build_bst(self, preorder: list[int]) -> TreeNode | None:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        split_idx = self.__first_gt_idx(preorder[0], preorder[1:])

        return TreeNode(
            preorder[0],
            self.__build_bst(preorder[1:split_idx]),
            self.__build_bst(preorder[split_idx:]),
        )

    def deserialize(self, data: str) -> TreeNode | None:
        return self.__build_bst([int(n) for n in data.split()])


codec = Codec()

tree1 = TreeNode(
    8,
    TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
    TreeNode(10, TreeNode(14, TreeNode(13))),
)

case1 = codec.serialize(tree1)
case1_out = codec.deserialize(case1)

tree2 = TreeNode(2, TreeNode(1))
case2 = codec.serialize(tree2)
case2_out = codec.deserialize(case2)

# 8 [3 1 6 4 7] [10 14 13]
