from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        if numRows == 1:
            return triangle

        def createRow(prevRow: List[int]): # assumes row >= 1 is passed
            newRowLen = len(prevRow)
            newRow = [1] * (newRowLen + 1)
            
            for i in range(1, newRowLen):
                newRow[i] = prevRow[i] + prevRow[i-1]
            return newRow


        for i in range(numRows - 1):
            triangle.append(createRow(triangle[i]))
        
        return triangle

print(Solution().generate(5))
