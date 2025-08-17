# https://leetcode.com/problems/new-21-game/


class Solution:
    def new21Game(self, n: int, k: int, max_pts: int) -> float:
        dp = [1.0] + [0] * n
        s = 1.0 if k > 0 else 0

        for pts in range(1, n + 1):
            dp[pts] = s / max_pts
            if pts < k:
                s += dp[pts]
            if pts - max_pts >= 0 and pts - max_pts < k:
                s -= dp[pts - max_pts]

        return sum(dp[k:])


if __name__ == "__main__":
    assert Solution().new21Game(10, 1, 10) == 1.0
    assert Solution().new21Game(6, 1, 10) == 0.6
    assert Solution().new21Game(21, 17, 10) == 0.73278
    assert Solution().new21Game(6, 5, 3) == 24 / 31
