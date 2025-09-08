# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

from itertools import count


class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        valid = filter(
            lambda x: "0" not in str(x) and "0" not in str(n - x),
            count(1),
        )

        x = next(valid)
        return [x, n - x]


if __name__ == "__main__":
    assert Solution().getNoZeroIntegers(2) == [1, 1]
    assert Solution().getNoZeroIntegers(11) == [2, 9]
