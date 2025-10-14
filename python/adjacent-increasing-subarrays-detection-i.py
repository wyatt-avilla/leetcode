# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/


class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        if (n := len(nums)) == 2:
            return True

        def is_strictly_increasing(nums: list[int]) -> bool:
            if (n := len(nums)) in {0, 1}:
                return True

            return all(nums[i - 1] < nums[i] for i in range(1, n))

        return any(
            is_strictly_increasing(nums[i : i + k])
            and is_strictly_increasing(nums[i + k : i + 2 * k])
            for i in range(n - 2 * k + 1)
        )


if __name__ == "__main__":
    assert Solution().hasIncreasingSubarrays([5, 8, -2, 1], 2)
    assert Solution().hasIncreasingSubarrays([19, 5], 1)
    assert Solution().hasIncreasingSubarrays([-15, 19], 1)
    assert Solution().hasIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3)
    assert not Solution().hasIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5)
