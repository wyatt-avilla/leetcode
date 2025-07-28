# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/


import operator
from collections.abc import Iterable
from functools import reduce
from itertools import chain, combinations


class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        def seq_or(s: Iterable[int]) -> int:
            return reduce(operator.or_, s)

        n = len(nums)
        max_or = seq_or(nums)

        subsets = chain.from_iterable(combinations(nums, i) for i in range(1, n + 1))

        return sum(seq_or(s) == max_or for s in subsets)


if __name__ == "__main__":
    assert Solution().countMaxOrSubsets([3, 2, 1, 5]) == 6
    assert Solution().countMaxOrSubsets([3, 1]) == 2
    assert Solution().countMaxOrSubsets([2, 2, 2]) == 7
