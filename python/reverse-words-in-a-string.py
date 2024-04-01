# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        word_list.reverse()
        print(word_list)
        return " ".join(word_list)


assert Solution().reverseWords("the sky is blue") == "blue is sky the"
assert Solution().reverseWords("  hello world  ") == "world hello"
assert Solution().reverseWords("a good   example") == "example good a"
