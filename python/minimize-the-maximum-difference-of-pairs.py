# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/


class Solution:
    def pairs_with_diff_leq_than(self, nums: list[int], t: int) -> int:
        count = 0

        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i + 1] - nums[i] <= t:
                count += 1
                i += 2
            else:
                i += 1

        return count

    def minimizeMax(self, nums: list[int], p: int) -> int:
        sorted_nums = sorted(nums)

        left = 0
        right = sorted_nums[-1] - sorted_nums[0]

        while left < right:
            mid = left + (right - left) // 2
            if self.pairs_with_diff_leq_than(sorted_nums, mid) >= p:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    assert Solution().minimizeMax([3, 4, 2, 3, 2, 1, 2], 3) == 1
    assert Solution().minimizeMax([10, 1, 2, 7, 1, 3], 2) == 1
    assert Solution().minimizeMax([4, 2, 1, 2], 1) == 0
    assert Solution().minimizeMax([0, 5, 3, 4], 0) == 0
    assert Solution().minimizeMax([0, 3, 3, 4], 0) == 0
