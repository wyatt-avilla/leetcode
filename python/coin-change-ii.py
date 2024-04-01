# https://leetcode.com/problems/coin-change-ii/

from __future__ import annotations


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        coins_len = len(coins)
        table_len = amount + 1
        table: list[list[int]] = [
            [0 for _ in range(coins_len)] for _ in range(table_len)
        ]
        for i in range(coins_len):  # always 1 way to make zero
            table[0][i] = 1

        for i in range(1, table_len):
            current_cell = table[i]
            if i % coins[0] == 0:
                current_cell[0] = 1
            for j in range(1, coins_len):
                current_coin = coins[j]
                if current_coin > i:
                    current_cell[j] = current_cell[j - 1]
                else:
                    current_cell[j] = current_cell[j - 1] + table[i - coins[j]][j]

        for i in range(table_len):
            print(f"{i} -> ( ", end="")
            for j in range(len(table[i])):
                print(f"{coins[j]}:{table[i][j]} ", end="")
            print(")")

        return table[amount][-1]


assert Solution().change(5, [1, 2, 5]) == 4
assert Solution().change(6, [1, 2, 5]) == 5
assert Solution().change(7, [1, 2, 5]) == 6
assert Solution().change(500, [1, 2, 5]) == 12701
assert Solution().change(8, [2, 3]) == 2
assert Solution().change(3, [2]) == 0
assert Solution().change(10, [10]) == 1
assert Solution().change(10, [5]) == 1
assert Solution().change(0, [7]) == 1
assert Solution().change(5, [1, 2, 5]) == 4
