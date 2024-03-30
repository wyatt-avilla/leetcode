# https://leetcode.com/problems/reshape-the-matrix/

from typing import List
from collections import deque
import itertools


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flattened = deque(list(itertools.chain(*mat)))
        reshaped = []

        if r * c != len(flattened):
            return mat

        for row in range(r):
            reshaped.append([])
            for col in range(c):
                reshaped[row].append(flattened.popleft())

        return reshaped


nlist = [[1, 2], [3, 4]]

print(Solution().matrixReshape(nlist, 2, 4))
