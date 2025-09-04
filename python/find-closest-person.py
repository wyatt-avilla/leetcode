# https://leetcode.com/problems/find-closest-person/


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        p1_dist = abs(z - x)
        p2_dist = abs(z - y)
        if p1_dist < p2_dist:
            return 1
        if p2_dist < p1_dist:
            return 2

        return 0


assert Solution().findClosest(2, 7, 4) == 1
assert Solution().findClosest(2, 5, 6) == 2
assert Solution().findClosest(1, 5, 3) == 0
