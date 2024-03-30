# https://leetcode.com/problems/number-of-boomerangs/

from typing import List
from math import hypot


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomerangs = 0
        adjPoints = {}
        for startPoint in points:
            currentPointDict = {}
            for endPoint in points:
                if startPoint == endPoint:
                    continue
                currentPointDict.update({tuple(endPoint): hypot(startPoint[0] - endPoint[0], startPoint[1] - endPoint[1])})
            adjPoints.update({tuple(startPoint): currentPointDict})
        
        for distances in adjPoints.values():
            currentDistances = list(distances.values())
            for distance in currentDistances:
                boomerangs += currentDistances.count(distance) - 1 if currentDistances.count(distance) >= 2 else 0
        
        return boomerangs


assert Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]) == 2
assert Solution().numberOfBoomerangs([[1,1],[2,2],[3,3]]) == 2
assert Solution().numberOfBoomerangs([[1,1]]) == 0
assert Solution().numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]) == 20

