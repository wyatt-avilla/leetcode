# https://leetcode.com/problems/min-cost-climbing-stairs/

from __future__ import annotations


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        cost_from_step = [0] * (n + 1)
        cost_from_step[-1] = 0
        cost_from_step[-2] = cost[-1]
        cost_from_step[-3] = cost[-2]

        for i in range(n - 3, -1, -1):
            cost_from_step[i] = cost[i] + min(
                cost_from_step[i + 1],
                cost_from_step[i + 2],
            )

        return min(cost_from_step[0], cost_from_step[1])


Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
