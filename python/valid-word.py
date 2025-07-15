# https://leetcode.com/problems/valid-word/

from string import ascii_lowercase


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        digits = {str(d) for d in range(10)}
        vowels = {"a", "e", "i", "o", "u"}
        consonants = set(ascii_lowercase) - vowels

        valid_chars = digits | vowels | consonants

        seen_vowel = seen_consonant = False
        for c in word.lower():
            if c not in valid_chars:
                return False

            if c in vowels:
                seen_vowel = True
            if c in consonants:
                seen_consonant = True

        return seen_vowel and seen_consonant


if __name__ == "__main__":
    assert Solution().isValid("234Adas")
    assert not Solution().isValid("b3")
    assert not Solution().isValid("a3$e")
