# https://leetcode.com/problems/elimination-game/

from __future__ import annotations


class Solution:
    def lastRemaining(self, n: int) -> int:
        arr = list(range(1, n + 1))
        return self.traverse(arr, "left")

    def traverse(self, arr: list, starting_from: str) -> int:
        current_len = len(arr)
        new_arr = []
        if current_len == 1:
            return arr[0]

        if current_len % 2 == 1 or starting_from == "left":
            new_arr = [arr[i] for i in range(current_len) if i % 2 == 1]
        elif starting_from == "right":
            new_arr = [arr[i] for i in range(current_len) if i % 2 == 0]

        starting_from = "right" if starting_from == "left" else "left"
        return self.traverse(new_arr, starting_from)


for i in range(1, 30):
    print(f"{i:2} : {Solution().lastRemaining(i)}")
p = [0] * 4
