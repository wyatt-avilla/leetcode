from bisect import bisect_left, bisect_right


class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], start_pos: int, k: int) -> int:
        n = len(fruits)
        prefix_sum = [0] * (n + 1)
        indices = [i for i, _ in fruits]

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + fruits[i][1]

        return max(
            max(
                prefix_sum[bisect_right(indices, start_pos + (k - 2 * x))]
                - prefix_sum[bisect_left(indices, start_pos - x)],
                prefix_sum[bisect_right(indices, start_pos + x)]
                - prefix_sum[bisect_left(indices, start_pos - (k - 2 * x))],
            )
            for x in range(k // 2 + 1)
        )


if __name__ == "__main__":
    assert Solution().maxTotalFruits([[2, 8], [6, 3], [8, 6]], 5, 4) == 9
    assert (
        Solution().maxTotalFruits(
            [[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]],
            5,
            4,
        )
        == 14
    )
    assert Solution().maxTotalFruits([[0, 3], [6, 4], [8, 5]], 3, 2) == 0
    assert Solution().maxTotalFruits([[200000, 10000]], 200000, 0) == 10000
    assert Solution().maxTotalFruits([[5, 10000]], 0, 200000) == 10000
    assert Solution().maxTotalFruits([[0, 10000]], 200000, 200000) == 10000
    assert (
        Solution().maxTotalFruits(
            [
                [1, 9],
                [2, 10],
                [3, 1],
                [5, 6],
                [6, 3],
                [8, 2],
                [9, 2],
                [11, 4],
                [18, 10],
                [22, 8],
                [25, 2],
                [26, 2],
                [30, 4],
                [31, 5],
                [33, 9],
                [34, 1],
                [39, 10],
            ],
            19,
            9,
        )
        == 22
    )
    assert (
        Solution().maxTotalFruits(
            [
                [17, 6],
                [21, 6],
                [22, 3],
                [26, 4],
                [27, 5],
                [33, 3],
                [37, 9],
                [39, 7],
                [40, 10],
            ],
            38,
            20,
        )
        == 41
    )
    assert (
        Solution().maxTotalFruits(
            [
                [1, 2],
                [2, 3],
                [4, 1],
                [6, 6],
                [8, 1],
                [21, 1],
                [24, 2],
                [26, 1],
                [29, 10],
            ],
            27,
            23,
        )
        == 15
    )
