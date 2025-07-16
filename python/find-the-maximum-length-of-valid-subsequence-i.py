# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/


class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        all_zeroes = 0
        all_ones = 0
        alternating = 0

        alt_seeking: int | None = None
        for num in nums:
            if num % 2 == 0:
                all_zeroes += 1
            else:
                all_ones += 1

            if alt_seeking is None or num % 2 == alt_seeking:
                alternating += 1
                alt_seeking = 1 if num % 2 == 0 else 0

        return max(all_zeroes, all_ones, alternating)


if __name__ == "__main__":
    assert Solution().maximumLength([1, 2, 3, 4]) == 4
    assert Solution().maximumLength([1, 2, 1, 1, 2, 1, 2]) == 6
    assert Solution().maximumLength([1, 3]) == 2
    assert Solution().maximumLength([4, 2, 6]) == 3
    assert Solution().maximumLength([0, 0, 6]) == 3
