from typing import List
from math import ceil

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        timeToArrive = []
        for i in range(len(dist)):
            timeToArrive.append(ceil(dist[i] / speed[i]))
        timeToArrive.sort()

        eliminated = len(timeToArrive)
        for i in range(eliminated):
            if timeToArrive[i] - i == 0:
                eliminated = i
                break
 
        return eliminated

d = [3, 2, 4]
s = [5, 3, 2]

print(Solution().eliminateMaximum(d,s))
