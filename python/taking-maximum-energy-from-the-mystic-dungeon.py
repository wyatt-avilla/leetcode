# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

from collections.abc import Iterable


class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        n = len(energy)

        def max_reverse_sum(r: Iterable[int]) -> int:
            ans = -1000
            acc = 0
            for i in r:
                acc += energy[i]
                ans = max(ans, acc)

            return ans

        return max(
            max_reverse_sum(r) for r in (reversed(range(s, n, k)) for s in range(k))
        )


if __name__ == "__main__":
    assert Solution().maximumEnergy([5, 2, -10, -5, 1], 3) == 3
    assert Solution().maximumEnergy([-2, -3, -1], 2) == -1
