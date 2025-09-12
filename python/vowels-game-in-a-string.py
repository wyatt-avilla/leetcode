# https://leetcode.com/problems/vowels-game-in-a-string/


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u"}
        vowel_count = sum(c in vowels for c in s.lower())

        return vowel_count > 0


if __name__ == "__main__":
    assert Solution().doesAliceWin("leetcoder")
    assert not Solution().doesAliceWin("bbcd")
