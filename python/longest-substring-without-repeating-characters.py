# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from __future__ import annotations


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_len = len(s)
        contained_shars: set[str] = set()
        longest_len: int = 0
        left: int = 0
        right: int = 0
        while right < str_len:
            current_char = s[right]
            if current_char not in contained_shars:
                contained_shars.add(current_char)
                right += 1
            else:
                contained_shars.remove(s[left])
                left += 1

            longest_len = max(longest_len, right - left)

        return longest_len


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
