class Solution(object):
    def LengthOfLastWord(self, s):
        print(len(s.split()[-1]))


test = Solution()

test.LengthOfLastWord("pls i an gaming  ")
