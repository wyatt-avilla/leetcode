# https://leetcode.com/problems/longest-subsequence-repeated-k-times/

import itertools
from collections import Counter, deque


class Solution:
    def is_subsequence(self, s: str, potential_sub: str) -> bool:
        it = iter(s)
        return all(c in it for c in potential_sub)

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        available_chars = sorted(
            itertools.chain.from_iterable(c for c, v in Counter(s).items() if v >= k),
            reverse=True,
        )

        ans = ""
        q = deque(available_chars)
        while q:
            curr = q.popleft()
            ans = max(ans, curr, key=lambda s: len(s))

            for c in available_chars:
                potential_sub = curr + c
                if self.is_subsequence(s, potential_sub * k):
                    q.append(potential_sub)

        return ans


if __name__ == "__main__":
    assert Solution().longestSubsequenceRepeatedK("bbabbabbbbabaababab", 3) == "bbbb"
    assert Solution().longestSubsequenceRepeatedK("bb", 2) == "b"
    assert Solution().longestSubsequenceRepeatedK("ab", 2) == ""
    assert Solution().longestSubsequenceRepeatedK("letsleetcode", 2) == "let"
