# https://leetcode.com/problems/reordered-power-of-2/

from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits_of_powers_in_range = {
            frozenset((("1", 1),)),
            frozenset((("2", 1),)),
            frozenset((("4", 1),)),
            frozenset((("8", 1),)),
            frozenset((("1", 1), ("6", 1))),
            frozenset((("3", 1), ("2", 1))),
            frozenset((("6", 1), ("4", 1))),
            frozenset((("1", 1), ("2", 1), ("8", 1))),
            frozenset((("2", 1), ("5", 1), ("6", 1))),
            frozenset((("5", 1), ("1", 1), ("2", 1))),
            frozenset((("1", 1), ("0", 1), ("2", 1), ("4", 1))),
            frozenset((("2", 1), ("0", 1), ("4", 1), ("8", 1))),
            frozenset((("4", 1), ("0", 1), ("9", 1), ("6", 1))),
            frozenset((("8", 1), ("1", 1), ("9", 1), ("2", 1))),
            frozenset((("1", 1), ("6", 1), ("3", 1), ("8", 1), ("4", 1))),
            frozenset((("3", 1), ("2", 1), ("7", 1), ("6", 1), ("8", 1))),
            frozenset((("6", 2), ("5", 2), ("3", 1))),
            frozenset((("1", 2), ("3", 1), ("0", 1), ("7", 1), ("2", 1))),
            frozenset((("2", 2), ("6", 1), ("1", 1), ("4", 2))),
            frozenset((("5", 1), ("2", 2), ("4", 1), ("8", 2))),
            frozenset(
                (("1", 1), ("0", 1), ("4", 1), ("8", 1), ("5", 1), ("7", 1), ("6", 1)),
            ),
            frozenset((("2", 2), ("0", 1), ("9", 1), ("7", 1), ("1", 1), ("5", 1))),
            frozenset((("4", 3), ("1", 1), ("9", 1), ("3", 1), ("0", 1))),
            frozenset((("8", 4), ("3", 1), ("6", 1), ("0", 1))),
            frozenset((("1", 2), ("6", 2), ("7", 3), ("2", 1))),
            frozenset((("3", 3), ("5", 2), ("4", 2), ("2", 1))),
            frozenset((("6", 2), ("7", 1), ("1", 1), ("0", 1), ("8", 2), ("4", 1))),
            frozenset((("1", 2), ("3", 1), ("4", 1), ("2", 2), ("7", 2), ("8", 1))),
            frozenset((("2", 1), ("6", 2), ("8", 1), ("4", 2), ("3", 1), ("5", 2))),
            frozenset(
                (
                    ("5", 1),
                    ("3", 1),
                    ("6", 1),
                    ("8", 1),
                    ("7", 1),
                    ("0", 1),
                    ("9", 1),
                    ("1", 1),
                    ("2", 1),
                ),
            ),
        }

        return frozenset(Counter(str(n)).items()) in digits_of_powers_in_range


if __name__ == "__main__":
    assert Solution().reorderedPowerOf2(1)
    assert not Solution().reorderedPowerOf2(10)
