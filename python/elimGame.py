from typing import List
"""unfinished at the moment. i just viewed the solution, and figured id attempt to solve this again when the solution isnt so fresh in my mind"""


class Solution:
    def lastRemaining(self, n: int) -> int:
        arr = [num for num in range(1, n+1)]
        return self.traverse(arr, "left")

    def traverse(self, arr: List, startingFrom: str) -> int:
        currentLen = len(arr)
        newArr = [] 
        if currentLen == 1:
            return arr[0]

        if currentLen % 2 == 1 or startingFrom == "left":
            newArr = [arr[i] for i in range(currentLen) if i % 2 == 1]
        elif startingFrom == "right":
            newArr = [arr[i] for i in range(currentLen) if i % 2 == 0]

        startingFrom = "right" if startingFrom == "left" else "left"
        return self.traverse(newArr, startingFrom)


# print(Solution().lastRemaining(5))

for i in range(1, 30):
    print(f"{i:2} : {Solution().lastRemaining(i)}")
p = [0] * 4
