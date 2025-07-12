# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

from functools import cache


class Solution:
    def earliestAndLatest(
        self,
        n: int,
        first_player: int,
        second_player: int,
    ) -> list[int]:
        @cache
        def dp(n: int, f: int, s: int) -> tuple[int, int]:
            if f + s == n + 1:
                return (1, 1)

            # F(n,f,s)=F(n,n+1-s,n+1-f)
            if f + s > n + 1:
                return dp(n, n + 1 - s, n + 1 - f)

            earliest, latest = 6, 0
            n_half = (n + 1) // 2

            if s <= n_half:
                # s On the left or in the middle
                for i in range(f):
                    for j in range(s - f):
                        x, y = dp(n_half, i + 1, i + j + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)
            else:
                # s on the right
                # s'
                s_prime = n + 1 - s
                mid = (n - 2 * s_prime + 1) // 2
                for i in range(f):
                    for j in range(s_prime - f):
                        x, y = dp(n_half, i + 1, i + j + mid + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)

            return (earliest + 1, latest + 1)

        # F(n,f,s) = F(n,s,f)
        if first_player > second_player:
            first_player, second_player = second_player, first_player

        earliest, latest = dp(n, first_player, second_player)
        dp.cache_clear()
        return [earliest, latest]


if __name__ == "__main__":
    assert Solution().earliestAndLatest(11, 2, 4) == [3, 4]
    assert Solution().earliestAndLatest(5, 1, 5) == [1, 1]
