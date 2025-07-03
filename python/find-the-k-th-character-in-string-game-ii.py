# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/


import math
from collections.abc import Generator
from string import ascii_lowercase


class Solution:
    @staticmethod
    def contributing_idxs(k: int) -> Generator[int, None, None]:
        while k > 0:
            yield k
            k -= 1 << (k.bit_length() - 1)
        yield 0

    def kthCharacter(self, k: int, operations: list[int]) -> str:
        chars_idxs = {c: i for i, c in enumerate(ascii_lowercase)}
        llen = len(ascii_lowercase)
        char = "a"

        if k == 1:
            return char

        idxs = list(reversed([*Solution.contributing_idxs(k - 1)]))

        for ops_needed in (math.floor(math.log2(x)) + 1 for x in idxs[1:]):
            next_op = operations[ops_needed - 1]

            if next_op == 1:
                char = ascii_lowercase[(chars_idxs[char] + 1) % llen]

        return char


if __name__ == "__main__":
    assert Solution().kthCharacter(22, [1, 1, 1, 1, 1]) == "d"
    assert Solution().kthCharacter(10, [0, 1, 0, 1]) == "b"
    assert Solution().kthCharacter(9, [0, 1, 0, 1]) == "b"
    assert Solution().kthCharacter(8, [0, 1, 0, 1]) == "b"
    assert Solution().kthCharacter(1, [0, 1, 0, 1]) == "a"
    assert Solution().kthCharacter(2, [0, 1, 0, 1]) == "a"
    assert Solution().kthCharacter(3, [0, 1, 0, 1]) == "b"
    assert Solution().kthCharacter(5, [0, 1, 0, 1]) == "a"
    assert Solution().kthCharacter(4, [0, 1, 0, 1]) == "b"
    assert Solution().kthCharacter(5, [0, 1, 0, 1]) == "a"
    assert Solution().kthCharacter(7, [0, 1, 0, 1]) == "b"
    assert Solution().kthCharacter(8, [0, 1, 0, 1]) == "b"
    assert Solution().kthCharacter(9, [0, 1, 0, 1]) == "b"
    assert Solution().kthCharacter(8, [1, 1, 1]) == "d"
    assert Solution().kthCharacter(1, [1, 0]) == "a"
    assert Solution().kthCharacter(5, [0, 0, 0]) == "a"
    assert Solution().kthCharacter(3, [1, 0]) == "a"
