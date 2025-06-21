# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/


from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqs = Counter(word)

        unique_chars = set(word)
        deletions = len(word)
        for fix_char in unique_chars:
            fix_freq = freqs[fix_char]

            curr_deletions = 0
            for freq in (f for c, f in freqs.items() if c != fix_char):
                if freq < fix_freq:
                    curr_deletions += freq
                elif freq > fix_freq + k:
                    curr_deletions += freq - fix_freq - k
                else:
                    curr_deletions += 0

            deletions = min(deletions, curr_deletions)

        return deletions


if __name__ == "__main__":
    assert Solution().minimumDeletions("aabcaba", 0) == 3
    assert Solution().minimumDeletions("aaabaaa", 2) == 1
    assert Solution().minimumDeletions("dabdcbdcdcd", 2) == 2
