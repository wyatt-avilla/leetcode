# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        prev_contig_size = 0
        gap_size = int(nums[0] == 0)
        contig_size = int(nums[0] == 1)
        prev_digit = nums[0]

        def ans_calc(contig_size: int) -> int:
            return max(ans, contig_size + (prev_contig_size if gap_size == 1 else 0))

        for i in range(1, n):
            curr = nums[i]
            if curr != prev_digit and curr == 0:
                ans = ans_calc(contig_size)
                prev_contig_size = contig_size
                contig_size = 0
                gap_size = 0

            if curr == 0:
                gap_size += 1
            else:
                contig_size += 1

            prev_digit = curr

        if contig_size > 0:
            ans = ans_calc(contig_size)

        return ans if ans < n else n - 1


if __name__ == "__main__":
    assert Solution().longestSubarray([1, 1, 0, 1]) == 3
    assert Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
    assert Solution().longestSubarray([1, 1, 1]) == 2
    assert Solution().longestSubarray([1, 0, 0]) == 1
    assert Solution().longestSubarray([0, 0, 1, 0]) == 1
    assert Solution().longestSubarray([1, 0, 0, 1]) == 1
