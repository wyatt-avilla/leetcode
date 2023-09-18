from math import ceil


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        loopLen = ceil(len(s)/2)
        sep = list(s)
        for i in range(loopLen):
            lChar = sep[i]
            rChar = sep[-i-1]
            if lChar != rChar:
                replacementChar = chr(min(ord(lChar), ord(rChar)))
                sep[i] = sep[-i-1] = replacementChar
        
        return "".join(sep)



inOuts = [
        ("egcfe", "efcfe"),
        ("abcd", "abba"),
        ("seven", "neven"),
        ]

for case in inOuts:
    inp, exp = case
    res = Solution().makeSmallestPalindrome(inp)
    if res != exp:
        print(f"{res} != {exp}")
