from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        costFromStep = [0] * (n + 1)
        costFromStep[-1] = 0
        costFromStep[-2] = cost[-1]
        costFromStep[-3] = cost[-2]

        for i in range(n-3, -1, -1):
            costFromStep[i] = cost[i] + min(costFromStep[i+1], costFromStep[i+2])

        return min(costFromStep[0], costFromStep[1])
        


Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])

