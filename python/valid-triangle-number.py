# https://leetcode.com/problems/valid-triangle-number

from bisect import bisect_left


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nats = sorted(x for x in nums if x > 0)
        n = len(nats)

        return sum(
            bisect_left(nats, nats[i] + nats[j]) - j - 1
            for i in range(n)
            for j in range(i + 1, n)
        )


if __name__ == "__main__":
    assert Solution().triangleNumber([2, 2, 3, 4]) == 3
    assert Solution().triangleNumber([0, 7, 0, 0]) == 0
    assert Solution().triangleNumber([4, 2, 3, 4]) == 4
