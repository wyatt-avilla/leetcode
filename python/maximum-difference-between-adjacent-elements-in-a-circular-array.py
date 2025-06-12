# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/


class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        return max(
            abs(p[0] - p[1]) for p in ((nums[0], nums[-1]), *zip(nums, nums[1:]))
        )


if __name__ == "__main__":
    assert Solution().maxAdjacentDistance([1, 2, 4]) == 3
    assert Solution().maxAdjacentDistance([-5, -10, -5]) == 5
