# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

from __future__ import annotations


def real_idx_from(min_char: list[str | int], start_idx: int) -> int:
    curr_idx = start_idx
    while isinstance(min_char[curr_idx], int):
        curr_idx = min_char[curr_idx]

    if start_idx != curr_idx:
        min_char[start_idx] = curr_idx
    return curr_idx


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        min_char: list[str | int] = ["" for _ in range(len(s1))]
        present_at: dict[str, int] = {}

        for i, (a, b) in enumerate(zip(s1, s2)):
            if a not in present_at and b not in present_at:
                present_at[a] = i
                present_at[b] = i
                min_char[i] = min(a, b)
            elif a in present_at and b in present_at and a != b:
                smaller = min(a, b)
                bigger = max(a, b)
                dest_idx = real_idx_from(min_char, present_at[smaller])
                source_idx = real_idx_from(min_char, present_at[bigger])
                if source_idx != dest_idx:
                    min_char[dest_idx] = min(min_char[dest_idx], min_char[source_idx])
                    min_char[source_idx] = dest_idx
            else:
                present_char = a if a in present_at else b
                absent_char = a if a not in present_at else b
                idx = real_idx_from(min_char, present_at[present_char])
                min_char[idx] = min(min_char[idx], absent_char)
                present_at[absent_char] = idx

        return "".join(
            min_char[real_idx_from(min_char, present_at[c])] if c in present_at else c
            for c in baseStr
        )


if __name__ == "__main__":
    assert Solution().smallestEquivalentString("babbbbb", "aabbbab", "xx") == "xx"
    assert Solution().smallestEquivalentString("hello", "world", "hold") == "hdld"
    assert Solution().smallestEquivalentString("parker", "morris", "parser") == "makkek"
    assert (
        Solution().smallestEquivalentString("leetcode", "programs", "sourcecode")
        == "aauaaaaada"
    )
