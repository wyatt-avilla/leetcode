from __future__ import annotations


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode = None,
        right: TreeNode = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        if self.left or self.right:
            return f"({self.val}) -> ({self.left}) ({self.right})"
        return f"{self.val}"
