from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coinsLen = len(coins)
        tableLen = amount + 1
        table: List[List[int]] = [[0 for _ in range(coinsLen)] for _ in range(tableLen)]
        for i in range(coinsLen): # always 1 way to make zero
            table[0][i] = 1

        for i in range(1, tableLen):
            currentCell = table[i]
            if i % coins[0] == 0:
                currentCell[0] = 1
            for j in range(1, coinsLen):
                currentCoin = coins[j]
                if currentCoin > i:
                    currentCell[j] = currentCell[j-1]
                else:
                    currentCell[j] = currentCell[j-1] + table[i-coins[j]][j]




        for i in range(0, tableLen):
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
