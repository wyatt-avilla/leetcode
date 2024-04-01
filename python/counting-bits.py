# https://leetcode.com/problems/counting-bits/

from __future__ import annotations


class Solution:
    def countBits(self, n: int) -> list[int]:
        def power_generator() -> int:
            n = 1
            while True:
                yield 2**n
                n += 1

        bit_representation = [0] * (n + 1)
        if n > 0:
            bit_representation[1] = 1

        range_generator = power_generator()
        next_range_start_index = next(range_generator)

        i = 2
        while i < (n + 1):
            if i == next_range_start_index:
                for j in range(i // 2, i):
                    bit_representation[i] = bit_representation[j]

                    if i >= n:
                        break
                    i += 1
                next_range_start_index = next(range_generator)
                continue

            binary_val = i
            bit_count = 0
            while binary_val > 0:
                if binary_val & 1 == 1:
                    bit_count += 1
                binary_val = binary_val >> 1

            bit_representation[i] = bit_count

            i += 1

        return bit_representation


print(Solution().countBits(20))
