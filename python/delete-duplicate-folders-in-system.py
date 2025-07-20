# https://leetcode.com/problems/delete-duplicate-folders-in-system/


from collections import Counter


class Trie:
    serial: str = ""
    children: dict[str, "Trie"]

    def __init__(self) -> None:
        self.children = {}


class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        root = Trie()

        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]

        freq: dict[str, int] = Counter()

        def populate_serialization_fields_and_frequencies(node: Trie) -> None:
            if not node.children:
                return

            v = []
            for folder, child in node.children.items():
                populate_serialization_fields_and_frequencies(child)
                v.append(folder + "(" + child.serial + ")")

            v.sort()
            node.serial = "".join(v)
            freq[node.serial] += 1

        populate_serialization_fields_and_frequencies(root)

        ans = []
        path = []

        def reconstruct_valid_paths(node: Trie) -> None:
            if freq[node.serial] > 1:
                return

            if path:
                ans.append(path[:])

            for folder, child in node.children.items():
                path.append(folder)
                reconstruct_valid_paths(child)
                path.pop()

        reconstruct_valid_paths(root)
        return ans


if __name__ == "__main__":
    assert {
        tuple(p)
        for p in Solution().deleteDuplicateFolder(
            [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]],
        )
    } == {("d",), ("d", "a")}

    assert {
        tuple(p)
        for p in Solution().deleteDuplicateFolder(
            [
                ["a"],
                ["c"],
                ["a", "b"],
                ["c", "b"],
                ["a", "b", "x"],
                ["a", "b", "x", "y"],
                ["w"],
                ["w", "y"],
            ],
        )
    } == {("c",), ("c", "b"), ("a",), ("a", "b")}

    assert {
        tuple(p)
        for p in Solution().deleteDuplicateFolder(
            [["a", "b"], ["c", "d"], ["c"], ["a"]],
        )
    } == {("c",), ("c", "d"), ("a",), ("a", "b")}
