# https://leetcode.com/problems/implement-trie-prefix-tree/


class TrieNode:
    def __init__(self) -> None:
        self.terminating = False
        self.children: dict[str, TrieNode] = {}

    def __repr__(self) -> str:
        return str(f"{self.terminating}->{self.children}")


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()

            curr_node = curr_node.children[c]
        curr_node.terminating = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]

        return curr_node.terminating

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for c in prefix:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")
    trie.insert("app")
    assert trie.search("app")
