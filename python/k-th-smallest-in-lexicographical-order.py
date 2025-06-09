# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/


def count_below(height: int) -> int:
    return int((1 - 10**height) / (1 - 10)) - 1


class Solution:
    def dfs(
        self,
        n: int,
        k: int,
        depth: int,
        seen: int,
        max_depth: int,
        acc: int,
    ) -> tuple[int, int]:
        if depth == max_depth:
            return (acc, 0)

        seen += 1
        if seen == k:
            return (acc, 0)

        rem_depth = max_depth - depth

        if acc < n // 10 ** (rem_depth - 1):
            below = count_below(rem_depth)
            if seen + below < k:
                return (0, seen + below)

        for i in range(10):
            if (next_acc := acc * 10 + i) > n:
                continue
            (ans, s) = self.dfs(n, k, depth + 1, seen, max_depth, next_acc)
            seen = s
            if ans > 0:
                return (ans, 0)

        return (0, seen)

    def findKthNumber(self, n: int, k: int) -> int:
        digits = [int(c) for c in str(n)]

        seen = 0
        for i in range(1, 10):
            (a, s) = self.dfs(n, k, 0, seen, len(digits), i)
            seen = s
            if a > 0:
                return a

        raise ValueError


if __name__ == "__main__":
    assert Solution().findKthNumber(25, 15) == 22
    assert Solution().findKthNumber(13, 2) == 10
    assert Solution().findKthNumber(102, 17) == 21
    assert Solution().findKthNumber(223, 115) == 201
    assert Solution().findKthNumber(2, 2) == 2
    assert Solution().findKthNumber(1, 1) == 1
    assert Solution().findKthNumber(4089173, 3098723) == 3788849

    # 102 := [
    #    1,
    #    10,
    #    100,
    #    101,
    #    102,
    #    11,
    #    12,
    #    13,
    #    14,
    #    15,
    #    16,
    #    17,
    #    18,
    #    19,
    #    2,
    #    20,
    #    21,
    #    22,
    #    23,
    #    24,
    #    .
    #    .
    #    .
