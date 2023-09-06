class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def validSubString(smallerWord: str, biggerWord: str, sub: str) -> bool:
            smallerLen = len(smallerWord)
            biggerLen = len(biggerWord)
            subLen = len(sub)
            smallTargetIndex = 0
            bigTargetIndex = 0
            for i in range(biggerLen):
                if i < smallerLen and smallTargetIndex > len(sub) and smallerWord[i] == sub[smallTargetIndex]:
                    smallTargetIndex += 1
                if bigTargetIndex > len(sub) and biggerWord[i] == sub[bigTargetIndex]:
                    bigTargetIndex += 1
            return subLen == smallTargetIndex == bigTargetIndex

        smallerWord, biggerWord = ((word1), word2) if len(word1) <= len(word2) else (word2, word1)
        sharedChars = [char for char in smallerWord if char in biggerWord]
        subStrings = [""]
        for string in subStrings:
            print(string)
            for char in sharedChars:
                possibleString = string + char
                print(possibleString)
                if validSubString(smallerWord, biggerWord, possibleString):
                    subStrings.append(possibleString)

        return max(len(string) for string in subStrings)


assert Solution().minDistance("sea", "eat") == 2
assert Solution().minDistance("leetcode", "etco") == 4
assert Solution().minDistance("intention", "execution") == 8
assert Solution().minDistance("mart", "karma") == 5
print(Solution().minDistance("altruistic", "algorithm"))
