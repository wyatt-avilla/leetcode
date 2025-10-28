# https://leetcode.com/problems/make-array-elements-equal-to-zero/


class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        def valid_from(zero_idx: int) -> int:
            a, b = sum(nums[:zero_idx]), sum(nums[zero_idx:])
            if a == b:
                return 2
            elif abs(a - b) == 1:
                return 1
            else:
                return 0

        return sum(valid_from(i) for i, v in enumerate(nums) if v == 0)


if __name__ == "__main__":
    assert Solution().countValidSelections([1, 0, 2, 0, 3]) == 2
    assert Solution().countValidSelections([2, 3, 4, 0, 4, 1, 0]) == 0
    assert Solution().countValidSelections([4, 0, 1, 1, 1, 1]) == 2
    assert Solution().countValidSelections([16, 13, 10, 0, 0, 0, 10, 6, 7, 8, 7]) == 3
