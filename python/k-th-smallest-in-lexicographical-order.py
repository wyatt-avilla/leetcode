# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/


class Solution:
    def between(self, n: int, p1: int, p2: int) -> int:
        steps = 0
        while p1 <= n:
            steps += min(n + 1, p2) - p1
            p1 *= 10
            p2 *= 10
        return steps

    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1

        while k > 0:
            steps = self.between(n, curr, curr + 1)

            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr


if __name__ == "__main__":
    assert Solution().findKthNumber(25, 15) == 22
    assert Solution().findKthNumber(13, 2) == 10
    assert Solution().findKthNumber(102, 17) == 21
    assert Solution().findKthNumber(223, 115) == 201
    assert Solution().findKthNumber(2, 2) == 2
    assert Solution().findKthNumber(1, 1) == 1
    assert Solution().findKthNumber(4089173, 3098723) == 3788849
