# https://leetcode.com/problems/reshape-the-matrix/

from __future__ import annotations

import itertools
from collections import deque


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        flattened = deque(list(itertools.chain(*mat)))
        reshaped = []

        if r * c != len(flattened):
            return mat

        for row in range(r):
            reshaped.append([])
            for _col in range(c):
                reshaped[row].append(flattened.popleft())

        return reshaped


nlist = [[1, 2], [3, 4]]

print(Solution().matrixReshape(nlist, 2, 4))
