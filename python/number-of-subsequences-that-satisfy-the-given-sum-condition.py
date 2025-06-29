# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans += 1 << (right - left)
                left += 1
            else:
                right -= 1

        return ans % (10**9 + 7)


if __name__ == "__main__":
    assert Solution().numSubseq([2, 3, 3, 4, 6, 7], 12) == 61
    assert Solution().numSubseq([3, 3, 6, 8], 10) == 6
    assert Solution().numSubseq([3, 5, 6, 7], 9) == 4
    assert Solution().numSubseq([3, 5, 4], 7) == 2
    assert Solution().numSubseq([7, 6, 5, 3], 9) == 4
