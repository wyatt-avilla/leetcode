# https://leetcode.com/problems/car-pooling/

from __future__ import annotations


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        occupancy_per_mile = [0 for mile in range(1001)]
        max_mile = 0

        for trip in trips:
            occupancy_per_mile[trip[1] : trip[2]] = [
                mile + trip[0] for mile in occupancy_per_mile[trip[1] : trip[2]]
            ]
            max_mile = max(trip[2], max_mile)

        return all(occupancy_per_mile[i] <= capacity for i in range(max_mile))


tt = [[2, 1, 5], [3, 3, 7]]
Solution().carPooling(tt, 4)
