# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

from collections import deque
from functools import cache


class Solution:
    @cache
    @staticmethod
    def gcd(a: int, b: int) -> int:
        return b if a == 0 else Solution.gcd(b % a, a)

    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        q = deque(nums)
        stack = [q.popleft()]

        while q:
            num = q.popleft()
            if (gcd := Solution.gcd(num, stack[-1])) > 1:
                stack.append(int(abs(num * stack.pop()) / gcd))
                while (
                    len(stack) > 1 and (gcd := Solution.gcd(stack[-1], stack[-2])) > 1
                ):
                    stack.append(int(abs(stack.pop() * stack.pop()) / gcd))
            else:
                stack.append(num)

        return stack


if __name__ == "__main__":
    assert Solution().replaceNonCoprimes([2, 3, 2, 3, 6, 6]) == [6]
    assert Solution().replaceNonCoprimes([2, 2, 1, 1, 3, 3, 3]) == [2, 1, 1, 3]
    assert Solution().replaceNonCoprimes([13, 13, 13, 13, 13, 13]) == [13]
    assert Solution().replaceNonCoprimes([6, 4, 3, 2, 7, 6, 2]) == [12, 7, 6]
    assert Solution().replaceNonCoprimes([517, 11, 121, 517, 3, 51, 3, 1887, 5]) == [
        5687,
        1887,
        5,
    ]
