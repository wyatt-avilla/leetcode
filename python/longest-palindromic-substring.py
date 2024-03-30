# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        strLen = len(s)
        palindromes = []
        for i in range(1, strLen):
            lIDX = rIDX = i
            if s[i-1] == s[i]:
                lIDX = i-1
                while (lIDX >= 0 and rIDX < strLen) and s[lIDX] == s[rIDX]:
                    lIDX -= 1
                    rIDX += 1
                palindromes.append(s[lIDX+1:rIDX])
                lIDX = rIDX = i

            while (lIDX >= 0 and rIDX < strLen) and s[lIDX] == s[rIDX]:
                lIDX -= 1
                rIDX += 1
            palindromes.append(s[lIDX+1:rIDX])

        palindromes.sort(key=len)
        return palindromes[-1] if len(palindromes) > 0 else s[0]

            


cases = [
        ("babad", 3),
        ("cbbd", 2),
        ("ccc", 3),
        ("aaaa", 4),
        ]

for case in cases:
    inp, expLen = case
    res = Solution().longestPalindrome(inp)
    if len(res) != expLen or res != "".join(list(reversed(res))):
        print(f"{res} should be of len {expLen}")
