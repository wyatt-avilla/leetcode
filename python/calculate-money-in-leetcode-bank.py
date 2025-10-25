# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

from itertools import chain, count, islice


class Solution:
    def totalMoney(self, n: int) -> int:
        return sum(
            islice(chain.from_iterable((i + j for j in range(7)) for i in count(1)), n),
        )


if __name__ == "__main__":
    assert Solution().totalMoney(4) == 10
    assert Solution().totalMoney(10) == 37
    assert Solution().totalMoney(20) == 96
