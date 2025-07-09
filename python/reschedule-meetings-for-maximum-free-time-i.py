# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/


class Solution:
    def maxFreeTime(
        self,
        event_time: int,
        k: int,
        start_time: list[int],
        end_time: list[int],
    ) -> int:
        def total_gaps_in(events: list[tuple[int, int]]) -> int:
            return sum(e2[0] - e1[1] for e1, e2 in zip(events, events[1:]))

        events = [(0, 0), *list(zip(start_time, end_time)), (event_time, event_time)]

        curr_gap = max_gap = total_gaps_in(events[: k + 2])
        for i in range(1, len(events) - 1 - k):
            curr_gap -= events[i][0] - events[i - 1][1]
            curr_gap += events[i + k + 1][0] - events[i + k][1]
            max_gap = max(max_gap, curr_gap)

        return max_gap


if __name__ == "__main__":
    assert Solution().maxFreeTime(5, 1, [1, 3], [2, 5]) == 2
    assert Solution().maxFreeTime(10, 1, [0, 2, 9], [1, 4, 10]) == 6
    assert Solution().maxFreeTime(5, 2, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]) == 0
    assert Solution().maxFreeTime(35, 2, [0, 2, 4, 8, 16], [1, 3, 5, 15, 32]) == 7
