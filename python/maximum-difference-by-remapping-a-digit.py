# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
from __future__ import annotations

from functools import reduce
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator


class Solution:
    def first_non_matching_idx(self, digits: list[int], matchee: int) -> int:
        for i, v in enumerate(digits):
            if v != matchee:
                return i

        return 0

    def number_from(self, digits: Iterator[int]) -> int:
        init = next(digits)
        return reduce(lambda x, y: (x * 10) + y, digits, init)

    def minMaxDifference(self, num: int) -> int:
        digits = [int(c) for c in str(num)]

        max_replacement_digit = digits[self.first_non_matching_idx(digits, 9)]
        min_replacement_digit = digits[self.first_non_matching_idx(digits, 0)]

        return self.number_from(
            (9 if d == max_replacement_digit else d for d in digits),
        ) - self.number_from(
            (0 if d == min_replacement_digit else d for d in digits),
        )


if __name__ == "__main__":
    assert Solution().minMaxDifference(11891) == 99009
    assert Solution().minMaxDifference(90) == 99
    assert Solution().minMaxDifference(99999) == 99999
