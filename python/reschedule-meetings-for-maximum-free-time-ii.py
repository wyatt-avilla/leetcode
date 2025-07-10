# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/


from bisect import bisect_left
from collections import defaultdict


class Solution:
    def maxFreeTime(
        self,
        event_time: int,
        start_time: list[int],
        end_time: list[int],
    ) -> int:
        bounds = [
            (0, 0),
            *zip(start_time, end_time),
            (event_time, event_time),
        ]

        gaps_and_starts_dict: dict[int, set[int]] = defaultdict(set)
        for gap, start in filter(
            lambda p: p[0] > 0,
            ((e2[0] - e1[1], e1[1]) for e1, e2 in zip(bounds, bounds[1:])),
        ):
            gaps_and_starts_dict[gap].add(start)

        gaps_and_starts = sorted(
            (key, frozenset(s)) for key, s in gaps_and_starts_dict.items()
        )

        n = len(bounds)
        ans = 0
        for i in range(1, n - 1):
            curr_event_size = bounds[i][1] - bounds[i][0]
            gap_without_curr = bounds[i + 1][0] - bounds[i - 1][1]
            valid_gap_starts = (
                starts
                for _, starts in gaps_and_starts[
                    bisect_left(gaps_and_starts, curr_event_size, key=lambda p: p[0]) :
                ]
            )

            if any(
                any(start not in {bounds[i][1], bounds[i - 1][1]} for start in starts)
                for starts in valid_gap_starts
            ):
                ans = max(ans, gap_without_curr)
            ans = max(ans, gap_without_curr - curr_event_size)

        return ans


if __name__ == "__main__":
    assert Solution().maxFreeTime(5, [1, 3], [2, 5]) == 2
    assert Solution().maxFreeTime(10, [0, 7, 9], [1, 8, 10]) == 7
    assert Solution().maxFreeTime(10, [0, 3, 7, 9], [1, 4, 8, 10]) == 6
    assert Solution().maxFreeTime(5, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]) == 0
    assert Solution().maxFreeTime(86, [22, 82], [66, 85]) == 38
    assert Solution().maxFreeTime(37, [5, 14, 27, 34], [13, 18, 31, 37]) == 16
    assert Solution().maxFreeTime(20, [2, 4, 6, 9, 18], [4, 6, 9, 16, 20]) == 4
