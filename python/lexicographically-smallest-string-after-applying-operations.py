# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        incremented = {str(n): str((n + a) % 10) for n in range(10)}

        def add_op(s: str) -> str:
            res = ""
            for i in range(n):
                res += s[i] if i % 2 == 0 else incremented[s[i]]
            return res

        def rot_op(s: str) -> str:
            return s[n - b :] + s[: n - b]

        seen = set()

        def dfs(s: str) -> None:
            if s in seen:
                return
            seen.add(s)
            dfs(add_op(s))
            dfs(rot_op(s))
            return

        dfs(s)
        return min(seen)


if __name__ == "__main__":
    assert Solution().findLexSmallestString("5525", 9, 2) == "2050"
    assert Solution().findLexSmallestString("74", 5, 1) == "24"
    assert Solution().findLexSmallestString("0011", 4, 2) == "0011"
