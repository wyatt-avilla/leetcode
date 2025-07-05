# https://leetcode.com/problems/find-lucky-integer-in-an-array/

from collections import Counter


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        return max(
            (
                p[0]
                for p in filter(lambda p: p[0] == p[1], reversed(Counter(arr).items()))
            ),
            default=-1,
        )


if __name__ == "__main__":
    assert Solution().findLucky([2, 2, 3, 4]) == 2
    assert Solution().findLucky([1, 2, 2, 3, 3, 3]) == 3
    assert Solution().findLucky([2, 2, 2, 3, 3]) == -1
