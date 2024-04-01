from __future__ import annotations


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        smaller_word, bigger_word = (
            (word1, word2) if len(word1) <= len(word2) else (word2, word1)
        )
        smaller_len = len(smaller_word)
        bigger_len = len(bigger_word)
        common_letters: set[str] = {
            word for word in word1 + word2 if word in word1 and word in word2
        }
        longest_sub_per_idx: list[list[tuple[int, int, int]]] = [
            [] for _ in range(smaller_len)
        ]
        for letter in common_letters:
            longest_sub_per_idx[0].append(
                (smaller_word.index(letter) + 1, bigger_word.index(letter) + 1, 1),
            )
        for i in range(1, smaller_len):
            for sub_string in longest_sub_per_idx[i - 1]:
                for char in common_letters:
                    smaller_start, bigger_start, sub_len = sub_string
                    smaller_after_sub = smaller_word[smaller_start:]
                    bigger_after_sub = bigger_word[bigger_start:]
                    if char in smaller_after_sub and char in bigger_after_sub:
                        longest_sub_per_idx[i].append(
                            (
                                smaller_start + smaller_after_sub.index(char) + 1,
                                bigger_start + bigger_after_sub.index(char) + 1,
                                sub_len + 1,
                            ),
                        )
        needed_deletions = smaller_len + bigger_len
        for i in range(smaller_len - 1, -1, -1):
            if len(longest_sub_per_idx[i]) > 0:
                needed_deletions -= 2 * longest_sub_per_idx[i][0][2]
                break
        return needed_deletions


test_cases = [
    ("sea", "eat", 2),
    ("leetcode", "etco", 4),
    ("intention", "execution", 8),
    ("reer", "lele", 4),
    ("mart", "karma", 5),
    ("a", "b", 2),
    (
        "ebvivhpfxoptspwianmuhmkmbhxkqbrbgpfwpfcjixzhsjmtsgrzfshvkrvoxvjpmmsrojnpgzqdyofvicscopak",
        "vxoumkmxbpcixzhtrfhxmnzqyvisp",
        2,
    ),
]

for case in test_cases:
    if Solution().minDistance(case[0], case[1]) != case[2]:
        print(
            f"diff ({case[0]} & {case[1]}) == {case[2]}, not {Solution().minDistance(case[0], case[1])}",
        )
