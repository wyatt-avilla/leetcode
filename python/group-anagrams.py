# https://leetcode.com/problems/group-anagrams/

from __future__ import annotations


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict_strs: dict[frozenset[tuple[str, int]], list[str]] = {}
        for word in strs:
            letter_counts = frozenset((char, word.count(char)) for char in word)
            if letter_counts in dict_strs:
                dict_strs[letter_counts].append(word)
            else:
                dict_strs[letter_counts] = [word]

        return list(dict_strs.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
