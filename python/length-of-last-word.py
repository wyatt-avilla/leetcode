# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def LengthOfLastWord(self, s: str) -> int:
        return (len(s.split()[-1]))


test = Solution().LengthOfLastWord("pls i am gaming")

print(test)
