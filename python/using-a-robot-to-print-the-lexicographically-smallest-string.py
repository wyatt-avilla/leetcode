# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")


class PositiveCounter:
    def __init__(self, it: Iterable[T]) -> None:
        self.counter = Counter(it)

    def dec(self, key: T) -> None:
        if self.counter[key] == 1:
            self.counter.pop(key)
        else:
            self.counter[key] -= 1

    def min_lex_key(self) -> T | None:
        return min(self.counter.keys(), default=None)


class Solution:
    def robotWithString(self, s: str) -> str:
        p: list[str] = []
        t: list[str] = []
        counter = PositiveCounter(s)

        for c in s:
            t.append(c)
            counter.dec(c)

            while (
                len(t) > 0 and counter.min_lex_key() and counter.min_lex_key() >= t[-1]
            ):
                p.append(t.pop())

        p.extend(reversed(t))
        return "".join(p)


if __name__ == "__main__":
    assert Solution().robotWithString("bac") == "abc"
    assert Solution().robotWithString("zzabba") == "aabbzz"
    assert Solution().robotWithString("aazba") == "aaabz"
    assert Solution().robotWithString("bdda") == "addb"
    assert Solution().robotWithString("zza") == "azz"
    assert Solution().robotWithString("cdab") == "abdc"
    assert Solution().robotWithString("cabd") == "abcd"
    assert Solution().robotWithString("vzhofnpo") == "fnohopzv"
