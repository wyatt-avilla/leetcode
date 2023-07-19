from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        occupancyPerMile = [0 for mile in range(1001)]
        maxMile = 0

        for trip in trips:
            occupancyPerMile[trip[1]:trip[2]] = [mile + trip[0] for mile in occupancyPerMile[trip[1]:trip[2]]]
            maxMile = max(trip[2], maxMile)

        for i in range(maxMile):
            if occupancyPerMile[i] > capacity:
                return False

        return True


tt = [[2,1,5], [3,3,7]]
Solution().carPooling(tt, 4)
