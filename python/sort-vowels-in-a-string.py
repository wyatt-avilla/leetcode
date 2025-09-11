# https://leetcode.com/problems/sort-vowels-in-a-string/


class Solution:
    def sortVowels(self, _s: str) -> str:
        s = list(_s)

        vowels = {
            "a",
            "A",
            "e",
            "E",
            "i",
            "I",
            "o",
            "O",
            "u",
            "U",
        }

        present_vowels = []
        vowel_idxs = []

        for i, c in enumerate(s):
            if c in vowels:
                present_vowels.append(c)
                vowel_idxs.append(i)

        present_vowels.sort(key=ord)
        for i, c in zip(vowel_idxs, present_vowels):
            s[i] = c

        return "".join(s)


if __name__ == "__main__":
    assert Solution().sortVowels("lEetcOde") == "lEOtcede"
    assert Solution().sortVowels("lYmpH") == "lYmpH"
