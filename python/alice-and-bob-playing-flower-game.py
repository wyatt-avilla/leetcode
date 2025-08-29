# https://leetcode.com/problems/alice-and-bob-playing-flower-game/


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        def odds_in_range(x: int) -> int:
            return x // 2 + (x % 2)

        def evens_in_range(x: int) -> int:
            return x // 2

        return odds_in_range(n) * evens_in_range(m) + (
            odds_in_range(m) * evens_in_range(n)
        )


if __name__ == "__main__":
    assert Solution().flowerGame(3, 2) == 3
    assert Solution().flowerGame(1, 1) == 0
