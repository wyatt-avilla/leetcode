# https://leetcode.com/problems/maximum-difference-between-increasing-elements/


class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        curr_min = nums[0]

        best = -1
        for x in nums:
            if x > curr_min:
                best = max(best, x - curr_min)
            curr_min = min(curr_min, x)

        return best


if __name__ == "__main__":
    assert Solution().maximumDifference([7, 1, 5, 4]) == 4
    assert Solution().maximumDifference([7, 7, 7, 7, 1, 5, 4]) == 4
    assert Solution().maximumDifference([9, 4, 3, 2]) == -1
    assert Solution().maximumDifference([1, 5, 2, 10]) == 9
    assert Solution().maximumDifference([7, 7, 2, 7, 1, 4, 5]) == 5
