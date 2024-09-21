from __future__ import annotations

from enum import Enum
from typing import Any, Callable


class TreeNode:
    class TraversalType(Enum):
        PREORDER = 0
        INORDER = 1
        POSTORDER = 2

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        if self.left or self.right:
            return f"({self.val}) -> ({self.left}) ({self.right})"
        return f"{self.val}"

    def dfs_map(
        self,
        func: Callable[[int], Any],
        trav: TraversalType = TraversalType.PREORDER,
    ) -> list[Any]:
        return self.__dfs_map(self, func, trav)

    def __dfs_map(
        self,
        node: TreeNode | None,
        func: Callable[[int], Any],
        trav: TraversalType,
    ) -> list[Any]:
        if node is None:
            return []

        match trav:
            case self.TraversalType.PREORDER:
                return [
                    func(self.val),
                    *self.__dfs_map(node.left, func, trav),
                    *self.__dfs_map(node.right, func, trav),
                ]
            case self.TraversalType.INORDER:
                return [
                    *self.__dfs_map(node.left, func, trav),
                    func(self.val),
                    *self.__dfs_map(node.right, func, trav),
                ]
            case self.TraversalType.POSTORDER:
                return [
                    *self.__dfs_map(node.left, func, trav),
                    *self.__dfs_map(node.right, func, trav),
                    func(self.val),
                ]
