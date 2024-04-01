# https://leetcode.com/problems/longest-consecutive-sequence/

from __future__ import annotations

from typing import list


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sorted_nums = sorted(set(nums))
        nums_len = len(sorted_nums)
        longest_sequence = 0
        current_sequence = 1
        for i in range(nums_len - 1):
            if sorted_nums[i + 1] == (sorted_nums[i] + 1):
                current_sequence += 1
            else:
                longest_sequence = max(current_sequence, longest_sequence)
                current_sequence = 1
        return max(current_sequence, longest_sequence) if nums_len >= 1 else 0


assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
assert Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
assert Solution().longestConsecutive([]) == 0
