# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from collections import defaultdict


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        available_pairs: defaultdict[str, int] = defaultdict(lambda: 0)

        length = 0
        for l, r in (tuple(w) for w in words):
            if available_pairs[r + l] == 0:
                available_pairs[l + r] += 1
            else:
                available_pairs[r + l] -= 1
                length += 4

        if any(
            l == r for l, r in (tuple(k) for k, v in available_pairs.items() if v > 0)
        ):
            length += 2
        return length


if __name__ == "__main__":
    assert Solution().longestPalindrome(["lc", "cl", "gg"]) == 6
    assert Solution().longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]) == 8
    assert Solution().longestPalindrome(["cl", "ll", "xx"]) == 2
