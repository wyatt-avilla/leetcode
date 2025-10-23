# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

from itertools import pairwise


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        return (
            s[0] == s[1]
            if len(s) == 2
            else self.hasSameDigits(
                "".join((str((int(a) + int(b)) % 10)) for a, b in pairwise(s)),
            )
        )


if __name__ == "__main__":
    assert Solution().hasSameDigits("3902")
    assert not Solution().hasSameDigits("34789")
