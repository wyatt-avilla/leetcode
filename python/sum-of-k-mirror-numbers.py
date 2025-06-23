# https://leetcode.com/problems/sum-of-k-mirror-numbers/

from collections.abc import Generator
from itertools import islice


class Solution:
    def palindromic_base10_numbers(self) -> Generator[int, None, None]:
        left, right = 1, 0
        while True:
            right = left * 10
            for div in (10, 1):
                for i in range(left, right):
                    combined = i
                    x = i // div
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    yield combined
            left = right

    def base_k(self, x: int, k: int) -> int:
        digits = []

        while x > 0:
            digits.append(x % k)
            x //= k

        return 0 if len(digits) == 0 else int("".join(str(d) for d in reversed(digits)))

    def is_mirror(self, num: int) -> bool:
        digits = list(str(num))
        return all(c1 == c2 for (c1, c2) in zip(digits, reversed(digits)))

    def kMirror(self, k: int, n: int) -> int:
        return sum(
            islice(
                (
                    num
                    for num in self.palindromic_base10_numbers()
                    if self.is_mirror((self.base_k(num, k)))
                ),
                n,
            )
        )


if __name__ == "__main__":
    assert Solution().kMirror(2, 5) == 25
    assert Solution().kMirror(3, 7) == 499
    assert Solution().kMirror(7, 17) == 20379000
