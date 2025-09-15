# https://leetcode.com/problems/maximum-number-of-words-you-can-type/


class Solution:
    def canBeTypedWords(self, text: str, broken_letters: str) -> int:
        broken_set = set(broken_letters)
        word_sets = [set(w) for w in text.split()]
        return sum(
            1 if len(broken_set & word_set) == 0 else 0 for word_set in word_sets
        )


if __name__ == "__main__":
    assert Solution().canBeTypedWords("hello world", "ad") == 1
    assert Solution().canBeTypedWords("leet code", "lt") == 1
    assert Solution().canBeTypedWords("leet code", "e") == 0
