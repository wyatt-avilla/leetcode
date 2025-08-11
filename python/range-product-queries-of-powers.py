# https://leetcode.com/problems/range-product-queries-of-powers/

import operator
from bisect import bisect_left
from functools import cache, reduce


class Solution:
    @cache
    @staticmethod
    def powers(x: int) -> list[int]:
        if x == 0:
            return [1]

        powers_in_range = (
            1,
            2,
            4,
            8,
            16,
            32,
            64,
            128,
            256,
            512,
            1024,
            2048,
            4096,
            8192,
            16384,
            32768,
            65536,
            131072,
            262144,
            524288,
            1048576,
            2097152,
            4194304,
            8388608,
            16777216,
            33554432,
            67108864,
            134217728,
            268435456,
            536870912,
            1073741824,
        )

        i = bisect_left(powers_in_range, x)
        if x - powers_in_range[i] == 0:
            return [x]

        return [*Solution.powers(x - powers_in_range[i - 1]), powers_in_range[i - 1]]

    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        powers = Solution.powers(n)

        return [
            reduce(
                operator.mul,
                powers[left : right + 1],
            )
            % (10**9 + 7)
            for left, right in queries
        ]


if __name__ == "__main__":
    assert Solution().productQueries(15, [[0, 1], [2, 2], [0, 3]]) == [2, 4, 64]
    assert Solution().productQueries(2, [[0, 0]]) == [2]
    assert Solution().productQueries(
        919,
        [
            [5, 5],
            [4, 4],
            [0, 1],
            [1, 5],
            [4, 6],
            [6, 6],
            [5, 6],
            [0, 3],
            [5, 5],
            [5, 6],
            [1, 2],
            [3, 5],
            [3, 6],
            [5, 5],
            [4, 4],
            [1, 1],
            [2, 4],
            [4, 5],
            [4, 4],
            [5, 6],
            [0, 4],
            [3, 3],
            [0, 4],
            [0, 5],
            [4, 4],
            [5, 5],
            [4, 6],
            [4, 5],
            [0, 4],
            [6, 6],
            [6, 6],
            [6, 6],
            [2, 2],
            [0, 5],
            [1, 4],
            [0, 3],
            [2, 4],
            [5, 5],
            [6, 6],
            [2, 2],
            [2, 3],
            [5, 5],
            [0, 6],
            [3, 3],
            [6, 6],
            [4, 4],
            [0, 0],
            [0, 2],
            [6, 6],
            [6, 6],
            [3, 6],
            [0, 4],
            [6, 6],
            [2, 2],
            [4, 6],
        ],
    ) == [
        256,
        128,
        2,
        4194304,
        16777216,
        512,
        131072,
        128,
        256,
        131072,
        8,
        524288,
        268435456,
        256,
        128,
        2,
        8192,
        32768,
        128,
        131072,
        16384,
        16,
        16384,
        4194304,
        128,
        256,
        16777216,
        32768,
        16384,
        512,
        512,
        512,
        4,
        4194304,
        16384,
        128,
        8192,
        256,
        512,
        4,
        64,
        256,
        147483634,
        16,
        512,
        128,
        1,
        8,
        512,
        512,
        268435456,
        16384,
        512,
        4,
        16777216,
    ]
