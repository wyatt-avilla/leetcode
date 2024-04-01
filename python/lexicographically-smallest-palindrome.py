# https://leetcode.com/problems/lexicographically-smallest-palindrome/

from math import ceil


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        loop_len = ceil(len(s) / 2)
        sep = list(s)
        for i in range(loop_len):
            lchar = sep[i]
            rchar = sep[-i - 1]
            if lchar != rchar:
                replacement_char = chr(min(ord(lchar), ord(rchar)))
                sep[i] = sep[-i - 1] = replacement_char

        return "".join(sep)


in_outs = [
    ("egcfe", "efcfe"),
    ("abcd", "abba"),
    ("seven", "neven"),
]

for case in in_outs:
    inp, exp = case
    res = Solution().makeSmallestPalindrome(inp)
    if res != exp:
        print(f"{res} != {exp}")
