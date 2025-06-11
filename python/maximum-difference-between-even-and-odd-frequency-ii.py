# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/
from __future__ import annotations

import math


class Solution:
    def parity_bits_for(self, a: int, b: int) -> int:
        return ((a & 1) << 1) | b & 1

    def max_diff_between(self, s: str, k: int, a: str, b: str) -> int:
        max_diff = -math.inf
        r_a_count = 0
        r_b_count = 0
        l_a_count = 0
        l_b_count = 0

        n = len(s)
        best: list[int | float] = [math.inf for _ in range(4)]

        l = -1
        for r in range(n):
            r_a_count += int(s[r] == a)
            r_b_count += int(s[r] == b)

            while r - l >= k and r_b_count - l_b_count >= 2:
                left_parity = self.parity_bits_for(l_a_count, l_b_count)

                best[left_parity] = min(best[left_parity], l_a_count - l_b_count)

                l += 1
                l_a_count += int(s[l] == a)
                l_b_count += int(s[l] == b)

            right_parity = self.parity_bits_for(r_a_count, r_b_count)

            need_parity = right_parity ^ 0b10

            if best[need_parity] != math.inf:
                max_diff = max(max_diff, r_a_count - r_b_count - best[need_parity])

        return max_diff if max_diff != math.inf else -math.inf

    def maxDifference(self, s: str, k: int) -> int:
        digits = ("0", "1", "2", "3", "4")
        return max(
            self.max_diff_between(s, k, *p)
            for p in ((i, j) for i in digits for j in digits if i != j)
        )


if __name__ == "__main__":
    assert Solution().maxDifference("1122211", 3) == 1
    assert Solution().maxDifference("12233", 4) == -1
    assert Solution().maxDifference("110", 3) == -1
