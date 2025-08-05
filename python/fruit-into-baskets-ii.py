# https://leetcode.com/problems/fruits-into-baskets-ii/


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        unplaced = 0
        for f in fruits:
            for i, b in enumerate(baskets):
                if b >= f:
                    baskets.pop(i)
                    break
            else:
                unplaced += 1

        return unplaced


if __name__ == "__main__":
    assert Solution().numOfUnplacedFruits([4, 2, 5], [3, 5, 4]) == 1
    assert Solution().numOfUnplacedFruits([3, 6, 1], [6, 4, 7]) == 0
