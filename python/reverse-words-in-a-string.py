# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        wordList.reverse()
        print(wordList)
        return " ".join(wordList)

assert Solution().reverseWords("the sky is blue") == "blue is sky the"
assert Solution().reverseWords("  hello world  ") == "world hello"
assert Solution().reverseWords("a good   example") == "example good a"
