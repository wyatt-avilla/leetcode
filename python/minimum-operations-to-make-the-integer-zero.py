# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

from itertools import count


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k, x in ((k, num1 - num2 * k) for k in count()):
            if k > x:
                return -1
            if k >= x.bit_count():
                return k

        return -1


if __name__ == "__main__":
    assert Solution().makeTheIntegerZero(3, -2) == 3
    assert Solution().makeTheIntegerZero(5, 0) == 2
    assert Solution().makeTheIntegerZero(5, 7) == -1
