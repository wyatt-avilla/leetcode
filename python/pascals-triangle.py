# https://leetcode.com/problems/pascals-triangle/

from __future__ import annotations


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        if numRows == 1:
            return triangle

        def create_row(prev_row: list[int]):  # assumes row >= 1 is passed
            new_row_len = len(prev_row)
            new_row = [1] * (new_row_len + 1)

            for i in range(1, new_row_len):
                new_row[i] = prev_row[i] + prev_row[i - 1]
            return new_row

        for i in range(numRows - 1):
            triangle.append(create_row(triangle[i]))

        return triangle


print(Solution().generate(5))
