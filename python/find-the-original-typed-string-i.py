# https://leetcode.com/problems/find-the-original-typed-string-i/


class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        contig = 0
        prev_char = ""
        for c in word:
            if c != prev_char:
                ans += contig
                contig = 0
                prev_char = c
            else:
                contig += 1
        ans += contig

        return ans


if __name__ == "__main__":
    assert Solution().possibleStringCount("aa") == 2
    assert Solution().possibleStringCount("aabbccccab") == 6
    assert Solution().possibleStringCount("abbcccc") == 5
    assert Solution().possibleStringCount("abcd") == 1
    assert Solution().possibleStringCount("aaaa") == 4
    assert Solution().possibleStringCount("ere") == 1
