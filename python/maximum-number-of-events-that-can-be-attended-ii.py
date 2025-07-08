# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

from bisect import bisect_left


class Solution:
    def maxValue(self, _events: list[list[int]], k: int) -> int:
        events = sorted((s, e, v) for s, e, v in _events)
        memo: dict[tuple[int, int], int] = {}

        def dfs(idx: int, included: int) -> int:
            if idx == len(events) or included == k:
                return 0
            if (idx, included) in memo:
                return memo[(idx, included)]

            _, new_end, val = events[idx]
            new_idx = bisect_left(events, (new_end + 1, 0, 0))

            ans = max(
                dfs(idx + 1, included),
                val + dfs(new_idx, included + 1),
            )

            memo[(idx, included)] = ans
            return ans

        return dfs(0, 0)


if __name__ == "__main__":
    assert Solution().maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2) == 7
    assert Solution().maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2) == 10
    assert Solution().maxValue([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 3) == 9
    assert (
        Solution().maxValue(
            [
                [19, 42, 7],
                [41, 73, 15],
                [52, 73, 84],
                [84, 92, 96],
                [6, 64, 50],
                [12, 56, 27],
                [22, 74, 44],
                [38, 85, 61],
            ],
            5,
        )
        == 187
    )
