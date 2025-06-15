# https://leitcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
from __future__ import annotations


class Solution:
    def first_non_matching_idx(self, digits: str, matchees: set[str]) -> int | None:
        for i, v in enumerate(digits):
            if v not in matchees:
                return i

        return None

    def maxDiff(self, num: int) -> int:
        digits = str(num)

        first_non_9_idx = self.first_non_matching_idx(digits, {"9"})
        if first_non_9_idx is None:
            first_non_9_idx = 0

        a = int(digits.replace(digits[first_non_9_idx], "9"))

        if digits[0] != "1":
            return a - int(digits.replace(digits[0], "1"))

        if (
            minimizing_replacement_idx := self.first_non_matching_idx(
                digits[1:],
                {"0", "1"},
            )
        ) is None:
            return a - num

        return a - int(digits.replace(digits[1 + minimizing_replacement_idx], "0"))


if __name__ == "__main__":
    assert Solution().maxDiff(123456) == 820000
    assert Solution().maxDiff(555) == 888
    assert Solution().maxDiff(9) == 8
    assert Solution().maxDiff(111) == 888
