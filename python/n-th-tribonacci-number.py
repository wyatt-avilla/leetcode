# https://leetcode.com/problems/n-th-tribonacci-number/

from functools import cache


class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n in {1, 2}:
            return 1

        return sum(self.tribonacci(x) for x in range(n - 3, n))


assert Solution().tribonacci(4) == 4
assert Solution().tribonacci(25) == 1389537
