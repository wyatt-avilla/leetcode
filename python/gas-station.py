# https://leetcode.com/problems/gas-station/

from __future__ import annotations


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        greedy_indices = [0] * n
        for index in range(n):
            greedy_indices[index] = gas[index] - cost[index]
        sorted_indices = sorted(range(n), key=lambda i: greedy_indices[i])
        sorted_indices.reverse()

        for index in sorted_indices:
            if gas[index] > 0:
                tank_capacity = 0
                for j in range(index, index + n + 1):
                    current_index = j % n
                    if j > index:
                        if current_index == index and tank_capacity >= 0:
                            return index
                        if tank_capacity <= 0:
                            break

                    tank_capacity += gas[current_index]
                    tank_capacity -= cost[current_index]

        return -1


assert Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
assert Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
assert Solution().canCompleteCircuit([1, 2, 3, 4, 5, 5, 70], [2, 3, 4, 3, 9, 6, 2]) == 6
