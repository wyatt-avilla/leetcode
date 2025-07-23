# https://leetcode.com/problems/maximum-score-from-removing-substrings/


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if len(s) <= 1:
            return 0
        if s == "ab":
            return x
        if s == "ba":
            return y

        def delete_all_subs(s: str, sub: str) -> str:
            if len(s) == 0:
                return ""

            stack = [s[0]]

            for c in s[1:]:
                if len(stack) > 0 and stack[-1] + c == sub:
                    stack.pop()
                else:
                    stack.append(c)

            return "".join(stack)

        opt_sub, other_sub = ("ab", "ba") if x > y else ("ba", "ab")

        s_del = delete_all_subs(s, opt_sub)
        points = (len(s) - len(s_del)) // 2 * max(x, y)

        return points + (
            len(s_del) - len(delete_all_subs(s_del, other_sub))
        ) // 2 * min(x, y)


if __name__ == "__main__":
    assert Solution().maximumGain("cdbcbbaaabab", 4, 5) == 19
    assert Solution().maximumGain("aabbaaxybbaabb", 5, 4) == 20
    assert Solution().maximumGain("cdbcbbaaabab", 4, 4) == 16
