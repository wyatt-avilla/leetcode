# https://leetcode.com/problems/gas-station/

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        greedyIndices = [0] * n
        for index in range(n):
            greedyIndices[index] = gas[index] - cost[index]
        sorted_indices = sorted(range(n), key=lambda i: greedyIndices[i])
        sorted_indices.reverse()

        for index in sorted_indices:
            if gas[index] > 0:
                tankCapacity = 0
                for j in range(index, index + n + 1):
                    currentIndex = j % n
                    if j > index:
                        if currentIndex == index and tankCapacity >= 0:
                            return index
                        if tankCapacity <= 0:
                            break

                    tankCapacity += gas[currentIndex]
                    tankCapacity -= cost[currentIndex]

        return -1





assert Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
assert Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
assert Solution().canCompleteCircuit([1, 2, 3, 4, 5, 5, 70], [2, 3, 4, 3, 9, 6, 2]) == 6
