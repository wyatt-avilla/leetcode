# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/


class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum(1 if "+" in op else -1 for op in operations)


if __name__ == "__main__":
    assert Solution().finalValueAfterOperations(["--X", "X++", "X++"]) == 1
    assert Solution().finalValueAfterOperations(["++X", "++X", "X++"]) == 3
    assert Solution().finalValueAfterOperations(["X++", "++X", "--X", "X--"]) == 0
