# https://leetcode.com/problems/divisor-game/

from __future__ import annotations


class Solution:
    def divisorGame(self, n: int) -> bool:
        def get_choice(n: int) -> int | None:
            factors = [
                x for x in range(n - 1, 0, -1) if n % x == 0
            ]  # factors in reverse order excluding number itself
            remainder = 1 if n % 2 == 0 else 0
            for num in factors:
                if n % num == 0 and num % 2 == remainder:
                    return num
            return None

        alice_wins = True
        while n > 0:
            x = get_choice(n)
            if not x:
                return not alice_wins

            n = n - x

            if alice_wins:
                alice_wins = False
                continue
            alice_wins = True

        return alice_wins


print(Solution().divisorGame(4))
