# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

from heapq import heappop, heappush


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        event_bounds = sorted((start, end) for start, end in events)
        n = len(events)
        max_day = max(end for start, end in events)

        heap: list[int] = []
        ans, j = 0, 0
        for i in range(1, max_day + 1):
            while j < n and event_bounds[j][0] <= i:
                heappush(heap, event_bounds[j][1])
                j += 1
            while heap and heap[0] < i:
                heappop(heap)
            if heap:
                heappop(heap)
                ans += 1

        return ans


if __name__ == "__main__":
    assert Solution().maxEvents([[1, 2], [2, 3], [3, 4]]) == 3
    assert Solution().maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]]) == 4
    assert Solution().maxEvents([[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]) == 5
    assert Solution().maxEvents([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]) == 4
    assert (
        Solution().maxEvents(
            [
                [25, 26],
                [19, 19],
                [9, 13],
                [16, 17],
                [17, 18],
                [20, 21],
                [22, 25],
                [11, 12],
                [19, 23],
                [7, 9],
                [1, 1],
                [21, 23],
                [14, 14],
                [4, 7],
                [16, 16],
                [24, 28],
                [16, 18],
                [4, 5],
                [18, 20],
                [16, 16],
                [25, 26],
            ],
        )
        == 19
    )
