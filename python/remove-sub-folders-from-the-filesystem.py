# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
from __future__ import annotations

from itertools import chain


class Trie:
    def __init__(self) -> None:
        self.prefixes: dict[str, Trie | None] = {}

    def __str__(self) -> str:
        return str(self.prefixes)


class Solution:
    @staticmethod
    def reconstruct_paths(trie: Trie | None, curr_path: str) -> list[str]:
        if trie is None:
            return [curr_path]

        return list(
            chain.from_iterable(
                Solution.reconstruct_paths(trie.prefixes[seg], curr_path + f"/{seg}")
                for seg in trie.prefixes
            ),
        )

    def removeSubfolders(self, folders: list[str]) -> list[str]:
        root = Trie()

        for folder in folders:
            node: Trie | None = root
            path_segments = [s for s in folder.split("/") if len(s) > 0]

            for i, seg in enumerate(path_segments):
                if node is None:
                    break

                if i == len(path_segments) - 1:
                    node.prefixes[seg] = None
                elif seg in node.prefixes:
                    node = node.prefixes[seg]
                else:
                    new_node = Trie()
                    node.prefixes[seg] = new_node
                    node = new_node

        return Solution.reconstruct_paths(root, "")


if __name__ == "__main__":
    assert Solution().removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]) == [
        "/a",
        "/c/d",
        "/c/f",
    ]
    assert Solution().removeSubfolders(["/a/b", "/a"]) == [
        "/a",
    ]
    assert Solution().removeSubfolders(["/a", "/a/b"]) == [
        "/a",
    ]

    assert Solution().removeSubfolders(["/a", "/a/b/c", "/a/b/d"]) == ["/a"]

    assert Solution().removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"]) == [
        "/a/b/c",
        "/a/b/ca",
        "/a/b/d",
    ]
