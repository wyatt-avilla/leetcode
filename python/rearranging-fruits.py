# https://leetcode.com/problems/rearranging-fruits/

from collections import Counter


class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        freq = Counter(basket1)
        for b2 in basket2:
            freq[b2] -= 1

        if any(v % 2 != 0 for v in freq.values()):
            return -1

        merge: list[int] = []
        for k, v in freq.items():
            merge.extend(k for _ in range(abs(v) // 2))

        merge.sort()

        min_cost = min(freq.keys())

        return sum(min(2 * min_cost, x) for x in merge[: len(merge) // 2])


if __name__ == "__main__":
    assert Solution().minCost([2, 3, 4, 1], [3, 2, 5, 1]) == -1
    assert Solution().minCost([4, 4, 1, 1, 3, 3], [2, 2, 2, 2, 5, 5]) == 5
    assert Solution().minCost([4, 2, 2, 2], [1, 4, 1, 2]) == 1
    assert Solution().minCost([4, 4, 1, 1], [2, 2, 2, 2]) == 3
    assert Solution().minCost([4, 4, 4, 4, 3], [5, 5, 5, 5, 3]) == 8
    assert (
        Solution().minCost(
            [84, 80, 43, 8, 80, 88, 43, 14, 100, 88],
            [32, 32, 42, 68, 68, 100, 42, 84, 14, 8],
        )
        == 48
    )
