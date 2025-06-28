# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

from collections import Counter


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        subseq_char_counts = dict(Counter(sorted(nums, reverse=True)[:k]).items())
        ans = []
        for n in nums:
            if n in subseq_char_counts:
                ans.append(n)
                subseq_char_counts[n] -= 1
                if subseq_char_counts[n] == 0:
                    del subseq_char_counts[n]

        return ans


if __name__ == "__main__":
    assert Solution().maxSubsequence([2, 1, 3, 3], 2) == [3, 3]
    assert Solution().maxSubsequence([-1, -2, 3, 4], 3) == [-1, 3, 4]
    assert Solution().maxSubsequence([3, 4, 3, 3], 2) == [3, 4]
