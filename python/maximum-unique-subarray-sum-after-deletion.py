# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/


class Solution:
    def maxSum(self, nums: list[int]) -> int:
        snums = set(nums)

        pos_nums = [n for n in snums if n > 0]

        return sum(pos_nums) if len(pos_nums) > 0 else max(snums)


if __name__ == "__main__":
    assert Solution().maxSum([1, 2, 3, 4, 5]) == 15
    assert Solution().maxSum([1, 1, 0, 1, 1]) == 1
    assert Solution().maxSum([1, 2, -1, -2, 1, 0, -1]) == 3
    assert Solution().maxSum([-100]) == -100
    assert Solution().maxSum([-100, -1]) == -100
