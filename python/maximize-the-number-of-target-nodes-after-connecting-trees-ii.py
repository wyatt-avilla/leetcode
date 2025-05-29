# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/
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

    def tag_nodes_by_parity(
        self,
        emap: dict[int, set[int]],
    ) -> tuple[set[int], set[int]]:
        even: set[int] = set()
        odd: set[int] = set()

        seed_parity = False

        def assign_node_parity(
            source: int, prev: int | None = None, *, curr_parity: bool
        ) -> None:
            if curr_parity == seed_parity:
                even.add(source)
            else:
                odd.add(source)

            for adj in emap[source] - {prev}:
                assign_node_parity(adj, source, curr_parity=not curr_parity)

        assign_node_parity(0, curr_parity=False)
        return (even, odd)

    def maxTargetNodes(
        self,
        edges1: list[list[int]],
        edges2: list[list[int]],
    ) -> list[int]:
        emap1 = self.outbound_from(tuple(e) for e in edges1)
        emap2 = self.outbound_from(tuple(e) for e in edges2)

        t1_even, t1_odd = self.tag_nodes_by_parity(emap1)
        t2_even, t2_odd = self.tag_nodes_by_parity(emap2)

        n = len(emap1)

        best_t2 = max(len(t2_odd), len(t2_even))
        even_best = len(t1_even) + best_t2
        odd_best = len(t1_odd) + best_t2

        return [even_best if i in t1_even else odd_best for i in range(n)]


if __name__ == "__main__":
    assert Solution().maxTargetNodes(
        [[0, 1], [0, 2], [2, 3], [2, 4]],
        [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
    ) == [8, 7, 7, 8, 8]

    assert Solution().maxTargetNodes(
        [[0, 1], [0, 2], [0, 3], [0, 4]],
        [[0, 1], [1, 2], [2, 3]],
    ) == [3, 6, 6, 6, 6]

    assert Solution().maxTargetNodes(
        [[2, 1], [7, 3], [0, 4], [7, 5], [2, 6], [0, 2], [0, 7]],
        [[3, 0], [1, 2], [5, 1], [6, 3], [9, 4], [5, 6], [7, 5], [9, 7], [8, 9]],
    ) == [11, 11, 9, 11, 9, 11, 11, 9]
