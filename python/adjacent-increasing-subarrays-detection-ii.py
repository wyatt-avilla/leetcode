# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

from itertools import pairwise


class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        seqs = []
        prev = nums[0] - 1
        contig = 0
        for num in nums:
            if num > prev:
                contig += 1
            else:
                seqs.append(contig)
                contig = 1
            prev = num
        seqs.append(contig)

        split_single = max(s // 2 for s in seqs)
        adj = max((min(a, b) for a, b in pairwise(seqs)), default=1)

        return max(split_single, adj)


if __name__ == "__main__":
    assert Solution().maxIncreasingSubarrays([-15, 19]) == 1
    assert Solution().maxIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1]) == 3
    assert Solution().maxIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7]) == 2
