# https://leetcode.com/problems/maximum-average-pass-ratio/

import heapq


class Ratio:
    def __init__(self, n: int, d: int) -> None:
        self.n = n
        self.d = d

    def negative_change(self) -> float:
        return -1 * (((self.n + 1) / (self.d + 1)) - (self.n / self.d))

    def as_float(self) -> float:
        return self.n / self.d

    def __lt__(self, other: "Ratio") -> bool:
        return self.negative_change() < other.negative_change()


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extra_students: int) -> float:
        heap: list[Ratio] = [Ratio(n, d) for n, d in classes]

        heapq.heapify(heap)

        for _ in range(extra_students):
            ratio = heapq.heappop(heap)
            heapq.heappush(heap, Ratio(ratio.n + 1, ratio.d + 1))

        return sum(r.as_float() for r in heap) / len(classes)


if __name__ == "__main__":
    assert Solution().maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2) == 0.78333
    assert Solution().maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4) == 0.53485
