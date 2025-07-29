# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/
from __future__ import annotations

import math
import operator
from functools import reduce


class Solution:
    @staticmethod
    def one_bit_idxs(n: int) -> list[int]:
        bits = Solution.bits_per_num(n)
        return [i for i in range(bits) if (1 << i) & n]

    @staticmethod
    def bits_per_num(n: int) -> int:
        return math.floor(math.log2(n) + 1) if n > 0 else 0

    @staticmethod
    def closest_next_bit(
        nums: list[int],
        total_bits: int,
    ) -> list[list[int | None]]:
        next_num_with_bit: list[list[int | None]] = [[None for i in range(total_bits)]]
        for i, n in enumerate(reversed(nums)):
            one_bit_idxs = set(Solution.one_bit_idxs(n))
            next_num_with_bit.append(
                [
                    len(nums) - i - 1
                    if bi in one_bit_idxs
                    else next_num_with_bit[-1][bi]
                    for bi in range(total_bits)
                ],
            )

        next_num_with_bit.reverse()
        next_num_with_bit.pop()

        return next_num_with_bit

    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        max_or = reduce(operator.or_, nums)
        bits = Solution.bits_per_num(max_or)

        next_num_with_bit = Solution.closest_next_bit(nums, bits)

        return [
            max((i for i in next_idxs if i is not None), default=i) - i + 1
            for i, next_idxs in enumerate(next_num_with_bit)
        ]


if __name__ == "__main__":
    assert Solution().smallestSubarrays([0, 3, 1, 2]) == [2, 1, 2, 1]
    assert Solution().smallestSubarrays([1, 0, 2, 1, 3]) == [3, 3, 2, 2, 1]
    assert Solution().smallestSubarrays([1, 2]) == [2, 1]
    assert Solution().smallestSubarrays([0]) == [1]
