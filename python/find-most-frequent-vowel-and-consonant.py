# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/


from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        counts = Counter(s)

        vmax = max((v for k, v in counts.items() if k in vowels), default=0)
        cmax = max((v for k, v in counts.items() if k not in vowels), default=0)

        return vmax + cmax


if __name__ == "__main__":
    assert Solution().maxFreqSum("successes") == 6
    assert Solution().maxFreqSum("aeiaeia") == 3
