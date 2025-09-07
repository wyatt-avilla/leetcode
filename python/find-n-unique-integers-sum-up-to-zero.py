# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

from itertools import chain
from math import ceil


class Solution:
    def sumZero(self, n: int) -> [int]:
        cancels = chain.from_iterable((i, -i) for i in range(1, ceil((n + 1) / 2)))

        return [0, *cancels] if n % 2 == 1 else list(cancels)


if __name__ == "__main__":
    assert sum(Solution().sumZero(7)) == 0
    assert sum(Solution().sumZero(6)) == 0
    assert sum(Solution().sumZero(4)) == 0
    assert sum(Solution().sumZero(5)) == 0
    assert sum(Solution().sumZero(3)) == 0
    assert sum(Solution().sumZero(1)) == 0
