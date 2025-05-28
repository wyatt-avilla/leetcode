# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/
from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


class Solution:
    def outbound_from(self, edges: Iterable[tuple[int, int]]) -> dict[int, set[int]]:
        d: dict[int, set[int]] = defaultdict(lambda: set())
        for a, b in edges:
            d[a].add(b)
            d[b].add(a)

        return dict(d)

    def dist_at_most_k_from(
        self,
        k: int,
        emap: dict[int, set[int]],
    ) -> dict[int, int]:
        def sum_adj_to_k(source: int, k: int, prev: int | None = None) -> int:
            return (
                0
                if k == 0
                else 1
                + sum(sum_adj_to_k(adj, k - 1, source) for adj in emap[source] - {prev})
            )

        return {source: sum_adj_to_k(source, k + 1) for source in emap}

    def maxTargetNodes(
        self,
        edges1: list[list[int]],
        edges2: list[list[int]],
        k: int,
    ) -> list[int]:
        edge1_map = self.outbound_from(tuple(e) for e in edges1)
        edge2_map = self.outbound_from(tuple(e) for e in edges2)

        dist_at_most_k_from = self.dist_at_most_k_from(k, edge1_map)
        best_edge2_count = max(self.dist_at_most_k_from(k - 1, edge2_map).values())

        n = len(edge1_map.keys())
        return [dist_at_most_k_from[i] + best_edge2_count for i in range(n)]


if __name__ == "__main__":
    assert Solution().maxTargetNodes(
        [[0, 1], [0, 2], [2, 3], [2, 4]],
        [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
        2,
    ) == [9, 7, 9, 8, 8]

    assert Solution().maxTargetNodes(
        [[0, 1], [0, 2], [0, 3], [0, 4]],
        [[0, 1], [1, 2], [2, 3]],
        1,
    ) == [6, 3, 3, 3, 3]
