from typing import List, Set, Tuple


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        smallerWord, biggerWord = (word1, word2) if len(word1) <= len(word2) else (word2, word1)
        smallerLen = len(smallerWord)
        biggerLen = len(biggerWord)
        commonLetters: Set[str] = {word for word in word1+word2 if word in word1 and word in word2}
        longestSubStringPerIdx: List[List[Tuple[int, int, int]]] = [[] for _ in range(smallerLen)]
        for letter in commonLetters:
            longestSubStringPerIdx[0].append((smallerWord.index(letter) + 1, biggerWord.index(letter) + 1, 1))
        for i in range(1, smallerLen):
            for subString in longestSubStringPerIdx[i-1]:
                for char in commonLetters:
                    smallerStart, biggerStart, subLen = subString
                    smallerAfterSub = smallerWord[smallerStart:]
                    biggerAfterSub = biggerWord[biggerStart:]
                    if char in smallerAfterSub and char in biggerAfterSub:
                        longestSubStringPerIdx[i].append((smallerStart + smallerAfterSub.index(char) + 1, biggerStart + biggerAfterSub.index(char) + 1, subLen + 1))
        neededDeletions = smallerLen + biggerLen
        for i in range(smallerLen-1, -1, -1):
            if len(longestSubStringPerIdx[i]) > 0:
                neededDeletions -= (2 * longestSubStringPerIdx[i][0][2])
                break
        return neededDeletions


testCases = [("sea", "eat", 2),
            ("leetcode", "etco", 4),
            ("intention", "execution", 8),
            ("reer", "lele", 4),
            ("mart", "karma", 5),
            ("a", "b", 2),
            ("ebvivhpfxoptspwianmuhmkmbhxkqbrbgpfwpfcjixzhsjmtsgrzfshvkrvoxvjpmmsrojnpgzqdyofvicscopak", "vxoumkmxbpcixzhtrfhxmnzqyvisp", 2),
             ]

for case in testCases:
    if Solution().minDistance(case[0], case[1]) != case[2]:
        print(f"diff ({case[0]} & {case[1]}) == {case[2]}, not {Solution().minDistance(case[0], case[1])}")
