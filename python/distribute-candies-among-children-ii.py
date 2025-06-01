# https://leetcode.com/problems/distribute-candies-among-children-ii/

from math import comb


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def fn(x: int) -> int:
            return comb(max(0, n - x * (limit + 1) + 2), 2)

        total_dists = comb(n + 2, 2)
        geq_one_over = 3 * fn(1)
        geq_two_over = 3 * fn(2)
        all_over = fn(3)

        return total_dists - geq_one_over + geq_two_over - all_over


if __name__ == "__main__":
    assert Solution().distributeCandies(5, 2) == 3
    assert Solution().distributeCandies(3, 3) == 10
