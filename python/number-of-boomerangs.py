# https://leetcode.com/problems/number-of-boomerangs/

from __future__ import annotations

from math import hypot


class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        boomerangs = 0
        adj_points = {}
        for start_point in points:
            current_point_dict = {}
            for end_point in points:
                if start_point == end_point:
                    continue
                current_point_dict.update(
                    {
                        tuple(end_point): hypot(
                            start_point[0] - end_point[0],
                            start_point[1] - end_point[1],
                        ),
                    },
                )
            adj_points.update({tuple(start_point): current_point_dict})

        for distances in adj_points.values():
            current_distances = list(distances.values())
            for distance in current_distances:
                boomerangs += (
                    current_distances.count(distance) - 1
                    if current_distances.count(distance) >= 2
                    else 0
                )

        return boomerangs


assert Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]) == 2
assert Solution().numberOfBoomerangs([[1, 1], [2, 2], [3, 3]]) == 2
assert Solution().numberOfBoomerangs([[1, 1]]) == 0
assert Solution().numberOfBoomerangs([[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]) == 20
