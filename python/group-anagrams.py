# https://leetcode.com/problems/group-anagrams/

from typing import List, Tuple, Dict, FrozenSet


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictStrs: Dict[FrozenSet[Tuple[str, int]], List[str]] = dict()
        for word in strs:
            letterCounts = frozenset((char, word.count(char)) for char in word)
            if letterCounts in dictStrs:
                dictStrs[letterCounts].append(word)
            else:
                dictStrs[letterCounts] = [word]

        return [words for words in dictStrs.values()]
        




print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
