# https://leetcode.com/problems/meeting-rooms-iii/

from heapq import heappop, heappush


class Solution:
    def mostBooked(self, n: int, _meetings: list[list[int]]) -> int:
        meetings_in = dict.fromkeys(range(n), 0)

        meetings = sorted((start, end) for start, end in _meetings)
        available_rooms = list(range(n))
        expiring_at: list[tuple[int, int]] = []

        for start, end in meetings:
            curr_time = start
            while len(expiring_at) > 0 and expiring_at[0][0] <= curr_time:
                _, room = heappop(expiring_at)
                heappush(available_rooms, room)

            if len(available_rooms) > 0:
                room = heappop(available_rooms)
                meetings_in[room] += 1
                heappush(expiring_at, (end, room))
            else:
                (time, room) = heappop(expiring_at)
                meetings_in[room] += 1
                heappush(expiring_at, (time + (end - start), room))

        return min(k for k, v in meetings_in.items() if v == max(meetings_in.values()))


if __name__ == "__main__":
    assert Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) == 0
    assert Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1
    assert Solution().mostBooked(2, [[1, 5], [4, 6], [5, 9], [10, 11]]) == 0
    assert Solution().mostBooked(2, [[1, 10], [5, 20], [30, 40], [35, 39]]) == 0
