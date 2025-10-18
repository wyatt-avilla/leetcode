# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/


class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        nums[0] -= k

        for i in range(1, n):
            nums[i] = min(max(nums[i] - k, nums[i - 1] + 1), nums[i] + k)

        return len(set(nums))


if __name__ == "__main__":
    assert Solution().maxDistinctElements([1, 2, 2, 3, 3, 4], 2) == 6
    assert Solution().maxDistinctElements([4, 4, 4, 4], 1) == 3
    assert Solution().maxDistinctElements([4, 4, 4, 4, 4, 4, 4, 4], 1) == 3
    assert Solution().maxDistinctElements([4], 1) == 1
    assert Solution().maxDistinctElements([1, 2, 3, 4, 5, 6, 7], 1) == 7
