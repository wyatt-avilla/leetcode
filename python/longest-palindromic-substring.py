# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        palindromes = []
        for i in range(1, str_len):
            l_idx = r_idx = i
            if s[i - 1] == s[i]:
                l_idx = i - 1
                while (l_idx >= 0 and r_idx < str_len) and s[l_idx] == s[r_idx]:
                    l_idx -= 1
                    r_idx += 1
                palindromes.append(s[l_idx + 1 : r_idx])
                l_idx = r_idx = i

            while (l_idx >= 0 and r_idx < str_len) and s[l_idx] == s[r_idx]:
                l_idx -= 1
                r_idx += 1
            palindromes.append(s[l_idx + 1 : r_idx])

        palindromes.sort(key=len)
        return palindromes[-1] if len(palindromes) > 0 else s[0]


cases = [
    ("babad", 3),
    ("cbbd", 2),
    ("ccc", 3),
    ("aaaa", 4),
]

for case in cases:
    inp, exp_len = case
    res = Solution().longestPalindrome(inp)
    if len(res) != exp_len or res != "".join(list(reversed(res))):
        print(f"{res} should be of len {exp_len}")
