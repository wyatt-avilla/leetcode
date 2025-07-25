# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

import math
import operator
from collections import defaultdict
from functools import reduce


class Solution:
    def score(self, part1: int, part2: int, part3: int) -> int:
        return max(part1, part2, part3) - min(part1, part2, part3)

    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        adj_list: dict[int, set[int]] = defaultdict(lambda: set())
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)

        tree_xor = reduce(operator.xor, nums)

        res = math.inf

        def dfs2(curr_node: int, prev_node: int, dfs1_xor: int, dfs1_node: int) -> int:
            curr_xor = reduce(
                lambda acc, n: acc ^ dfs2(n, curr_node, dfs1_xor, dfs1_node),
                (n for n in adj_list[curr_node] if n != prev_node),
                nums[curr_node],
            )

            if prev_node == dfs1_node:
                return curr_xor

            nonlocal res
            res = min(
                res,
                self.score(dfs1_xor, curr_xor, tree_xor ^ dfs1_xor ^ curr_xor),
            )
            return curr_xor

        def dfs(curr_node: int, prev_node: int) -> int:
            curr_xor = reduce(
                lambda acc, n: acc ^ dfs(n, curr_node),
                (n for n in adj_list[curr_node] if n != prev_node),
                nums[curr_node],
            )

            if prev_node in adj_list[curr_node]:
                dfs2(prev_node, curr_node, curr_xor, curr_node)

            return curr_xor

        dfs(0, -1)
        return int(res)


if __name__ == "__main__":
    assert (
        Solution().minimumScore([1, 5, 5, 4, 11], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 9
    )

    assert (
        Solution().minimumScore(
            [28, 24, 29, 16, 31, 31, 17, 18],
            [[0, 1], [6, 0], [6, 5], [6, 7], [3, 0], [2, 1], [2, 4]],
        )
        == 8
    )

    assert (
        Solution().minimumScore(
            [5, 5, 2, 4, 4, 2],
            [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]],
        )
        == 0
    )
