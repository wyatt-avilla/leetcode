# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/


from itertools import count
from math import ceil, floor, log


class Solution:
    @staticmethod
    def zero_range(left: int, right: int) -> int:
        acc = 0
        for power in count(floor(log(left, 4))):
            if (x := max(left, 4**power)) > right:
                break

            acc += (min(right, 4 ** (power + 1) - 1) - x + 1) * (power + 1)

        return ceil(acc / 2)

    def minOperations(self, queries: list[list[int]]) -> int:
        return sum(Solution.zero_range(left, right) for left, right in queries)


if __name__ == "__main__":
    assert Solution().minOperations([[1, 8]]) == 7
    assert Solution().minOperations([[2, 6]]) == 4
    assert Solution().minOperations([[1, 2], [2, 4]]) == 3
