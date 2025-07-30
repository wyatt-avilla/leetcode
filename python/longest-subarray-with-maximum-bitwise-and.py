# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_and = max(nums)

        in_block = nums[0] == max_and
        sub_count = ans = int(in_block)
        for num in nums[1:]:
            if num == max_and:
                in_block = True
                sub_count += 1
                ans = max(ans, sub_count)
            else:
                in_block = False
                sub_count = 0

        return ans


if __name__ == "__main__":
    assert Solution().longestSubarray([1, 2, 3, 3, 2, 2]) == 2
    assert Solution().longestSubarray([1, 2, 3, 4]) == 1
    assert Solution().longestSubarray([100, 5, 5]) == 1
    assert (
        Solution().longestSubarray(
            [
                311155,
                311155,
                311155,
                311155,
                311155,
                311155,
                311155,
                311155,
                201191,
                311155,
            ],
        )
        == 8
    )
