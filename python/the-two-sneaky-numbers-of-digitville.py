# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/


from collections import Counter


class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        return [k for k, v in Counter(nums).items() if v == 2]


if __name__ == "__main__":
    assert Solution().getSneakyNumbers([0, 1, 1, 0]) == [0, 1]
    assert Solution().getSneakyNumbers([0, 3, 2, 1, 3, 2]) == [2, 3]
    assert Solution().getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]) == [4, 5]
