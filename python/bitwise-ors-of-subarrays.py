# https://leetcode.com/problems/bitwise-ors-of-subarrays/


class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        ans: set[int] = set()

        frontier = {0}
        for x in arr:
            frontier = {x | y for y in frontier} | {x}
            ans |= frontier

        return len(ans)


if __name__ == "__main__":
    assert Solution().subarrayBitwiseORs([1, 1, 2]) == 3
    assert Solution().subarrayBitwiseORs([0]) == 1
    assert Solution().subarrayBitwiseORs([1, 2, 4]) == 6
    assert Solution().subarrayBitwiseORs([1, 3, 8, 7, 5, 4, 2]) == 10
