# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

from collections import defaultdict


class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        longest_sub_ending_with_rems: dict[tuple[int, int], int] = defaultdict(int)
        for n in nums:
            curr_rem = n % k
            for target_rem in range(k):
                prev_rem = (k + target_rem - curr_rem) % k
                longest_sub_ending_with_rems[(prev_rem, curr_rem)] = (
                    1 + longest_sub_ending_with_rems[(curr_rem, prev_rem)]
                )

        return max(longest_sub_ending_with_rems.values())


if __name__ == "__main__":
    assert Solution().maximumLength([1, 4, 2, 3, 1, 4], 3) == 4
    assert Solution().maximumLength([1, 2, 3, 4, 5], 2) == 5
    assert Solution().maximumLength([0, 1, 4, 2, 3, 1, 4], 3) == 4
    assert Solution().maximumLength([2, 1, 4, 1, 3], 3) == 3
