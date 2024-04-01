# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

from __future__ import annotations

from math import ceil


class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        time_to_arrive = [ceil(dist[i] / speed[i]) for i in range(len(dist))]
        time_to_arrive.sort()

        eliminated = len(time_to_arrive)
        for i in range(eliminated):
            if time_to_arrive[i] - i == 0:
                eliminated = i
                break

        return eliminated


d = [3, 2, 4]
s = [5, 3, 2]

print(Solution().eliminateMaximum(d, s))
