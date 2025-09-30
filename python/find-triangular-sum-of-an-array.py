# https://leetcode.com/problems/find-triangular-sum-of-an-array/


class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        return (
            nums[0]
            if len(nums) == 1
            else Solution().triangularSum(
                [(a + b) % 10 for a, b in zip(nums, nums[1:])],
            )
        )


if __name__ == "__main__":
    assert Solution().triangularSum([1, 2, 3, 4, 5])
    assert Solution().triangularSum([5]) == 5
