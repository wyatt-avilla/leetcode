# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

from itertools import pairwise


class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        return sum(
            a * b
            for a, b in pairwise(filter(lambda c: c > 0, (s.count("1") for s in bank)))
        )


if __name__ == "__main__":
    assert (
        Solution().numberOfBeams(
            [
                "011001",
                "000000",
                "010100",
                "001000",
            ],
        )
        == 8
    )

    assert (
        Solution().numberOfBeams(
            [
                "000",
                "111",
                "000",
            ],
        )
        == 0
    )
