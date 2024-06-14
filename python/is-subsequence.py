# https://leetcode.com/problems/is-subsequence/

from __future__ import annotations


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            slice_start: int = t.find(char)
            if slice_start == -1:
                return False
            t = t[slice_start + 1 :]

        return True


solution = Solution()

print(solution.isSubsequence("abc", "ahbgdc"))
print(solution.isSubsequence("axc", "ahbgdc"))
