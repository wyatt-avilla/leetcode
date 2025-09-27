# https://leetcode.com/problems/largest-triangle-area/

from itertools import product


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        def shoelace(
            a: tuple[int, int],
            b: tuple[int, int],
            c: tuple[int, int],
        ) -> float:
            x1, y1 = a
            x2, y2 = b
            x3, y3 = c

            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        return max(shoelace(a, b, c) for a, b, c in product(points, repeat=3))


if __name__ == "__main__":
    assert Solution().largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]) == 2
    assert Solution().largestTriangleArea([[1, 0], [0, 0], [0, 1]]) == 0.5
