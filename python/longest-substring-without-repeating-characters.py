# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from typing import Set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strLen = len(s)
        containedChars: Set[str] = set()
        longestLen: int = 0
        left: int = 0
        right: int = 0
        while right < strLen:
            currentChar = s[right]
            if currentChar not in containedChars:
                containedChars.add(currentChar)
                right += 1
            else:
                containedChars.remove(s[left])
                left += 1

            longestLen = max(longestLen, right-left)

        return longestLen




cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("", 0),
        ("pwwkew", 3),
        ]

for case in cases:
    inp, exp = case
    res = Solution().lengthOfLongestSubstring(inp)
    if res != exp:
        print(f"{inp} should yield {exp}, not {res}")
