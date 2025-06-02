# https://leetcode.com/problems/candy/


class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)

        dist: list[int] = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                dist[i] = dist[i - 1] + 1

        for i in reversed(range(n - 1)):
            if ratings[i] > ratings[i + 1]:
                dist[i] = max(dist[i], dist[i + 1] + 1)

        return sum(dist)


if __name__ == "__main__":
    assert Solution().candy([6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 0]) == 42
    assert (
        Solution().candy([100, 80, 70, 60, 70, 80, 90, 100, 90, 80, 70, 60, 60]) == 35
    )
    assert Solution().candy([1, 0, 2]) == 5
    assert Solution().candy([1, 2, 2]) == 4
    assert Solution().candy([1, 3, 4, 5, 2]) == 11
    assert (
        Solution().candy(
            [
                20000,
                20000,
                16001,
                16001,
                16002,
                16002,
                16003,
                16003,
                16004,
                16004,
                16005,
                16005,
                16006,
                16006,
                16007,
                16007,
                16008,
                16008,
                16009,
                16009,
                16010,
                16010,
                16011,
                16011,
                16012,
                16012,
                16013,
                16013,
                16014,
                16014,
                16015,
                16015,
                16016,
                16016,
                16017,
                16017,
                16018,
                16018,
                16019,
                16019,
                16020,
                16020,
                16021,
                16021,
                16022,
                16022,
                16023,
                16023,
                16024,
                16024,
            ]
        )
        == 74
    )
