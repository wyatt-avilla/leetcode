# https://leetcode.com/problems/24-game/
from __future__ import annotations

import contextlib

# ruff: noqa: S307
import itertools


class Solution:
    @staticmethod
    def eval_with_parens(
        nums: tuple[int, int, int, int],
        ops: tuple[str, str, str],
    ) -> list[int | float]:
        x, y, z, w = nums
        a, b, c = ops
        paren_perms = (
            f"{x}{a}{y}{b}{z}{c}{w}",
            f"({x}{a}{y}){b}{z}{c}{w}",
            f"{x}{a}({y}{b}{z}){c}{w}",
            f"{x}{a}{y}{b}({z}{c}{w})",
            f"({x}{a}{y}){b}({z}{c}{w})",
            f"({x}{a}{y}{b}{z}){c}{w}",
            f"{x}{a}({y}{b}{z}{c}{w})",
            f"(({x}{a}{y}){b}{z}){c}{w}",
            f"({x}{a}({y}{b}{z})){c}{w}",
            f"{x}{a}(({y}{b}{z}){c}{w})",
            f"{x}{a}({y}{b}({z}{c}{w}))",
        )

        ans = []
        for p in paren_perms:
            with contextlib.suppress(ZeroDivisionError):
                ans.append(eval(p))

        return ans

    def judgePoint24(self, cards: list[int]) -> bool:
        card_perms = itertools.permutations(cards)
        op_perms = itertools.product(("+", "-", "*", "/"), repeat=3)

        evals = (
            Solution.eval_with_parens(nums, ops)
            for nums, ops in itertools.product(card_perms, op_perms)
        )

        return any(abs(x - 24) < 0.01 for x in itertools.chain(*evals))


if __name__ == "__main__":
    assert Solution().judgePoint24([4, 1, 8, 7])
    assert not Solution().judgePoint24([1, 2, 1, 2])
    assert Solution().judgePoint24([1, 3, 4, 6])
    assert Solution().judgePoint24([3, 3, 8, 8])
