# https://leetcode.com/problems/find-the-original-typed-string-ii/

from collections.abc import Generator
from functools import reduce
from operator import mul


class Solution:
    def contig_sizes(self, word: str) -> Generator[int, None, None]:
        contig = 1
        prev_char = ""
        for c in word:
            if c != prev_char:
                if prev_char == "":
                    prev_char = c
                    continue

                yield contig
                contig = 1
                prev_char = c
            else:
                contig += 1
        yield contig

    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 1000000007
        contig_block_sizes = list(self.contig_sizes(word))
        ans = reduce(mul, contig_block_sizes) % mod

        if len(contig_block_sizes) >= k:
            return ans

        f, g = [1] + [0] * (k - 1), [1] * k
        for i in range(len(contig_block_sizes)):
            f_new = [0] * k
            for j in range(1, k):
                f_new[j] = g[j - 1]
                if j - contig_block_sizes[i] - 1 >= 0:
                    f_new[j] = (f_new[j] - g[j - contig_block_sizes[i] - 1]) % mod
            g_new = [f_new[0]] + [0] * (k - 1)
            for j in range(1, k):
                g_new[j] = (g_new[j - 1] + f_new[j]) % mod
            f, g = f_new, g_new
        return (ans - g[k - 1]) % mod


if __name__ == "__main__":
    assert Solution().possibleStringCount("aabbccdd", 7) == 5
    assert Solution().possibleStringCount("aabbccdd", 8) == 1
    assert Solution().possibleStringCount("aaabbb", 3) == 8
