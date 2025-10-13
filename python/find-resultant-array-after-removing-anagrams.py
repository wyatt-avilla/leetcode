# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

import itertools
from collections import Counter


class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        counts = [(i, Counter(word)) for i, word in enumerate(words)]

        while (
            tup := next(
                filter(
                    lambda t: t[1][0][1] == t[1][1][1],
                    enumerate(itertools.pairwise(counts)),
                ),
                None,
            )
        ) is not None:
            counts.pop(tup[0] + 1)

        return [words[i] for i, _ in counts]


if __name__ == "__main__":
    assert Solution().removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"]) == [
        "abba",
        "cd",
    ]
    assert Solution().removeAnagrams(["a", "b", "c", "d", "e"]) == [
        "a",
        "b",
        "c",
        "d",
        "e",
    ]
