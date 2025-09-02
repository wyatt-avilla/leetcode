# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/


class Solution:
    @staticmethod
    def in_bounds(
        top_left: tuple[int, int],
        bot_right: tuple[int, int],
        inner: tuple[int, int],
    ) -> bool:
        return (
            inner[0] >= top_left[0]
            and inner[0] <= bot_right[0]
            and inner[1] >= bot_right[1]
            and inner[1] <= top_left[1]
        )

    @staticmethod
    def upper_left(top_left: tuple[int, int], bot_right: tuple[int, int]) -> bool:
        return top_left[0] <= bot_right[0] and top_left[1] >= bot_right[1]

    def numberOfPairs(self, points: list[list[int]]) -> int:
        point_tups: list[tuple[int, int]] = [(a, b) for a, b in points]

        return sum(
            not any(Solution.in_bounds(a, b, c) for c in point_tups if c not in (a, b))
            for a in point_tups
            for b in point_tups
            if a != b and Solution().upper_left(a, b)
        )


if __name__ == "__main__":
    assert Solution().numberOfPairs([[1, 1], [2, 2], [3, 3]]) == 0
    assert Solution().numberOfPairs([[6, 2], [4, 4], [2, 6]]) == 2
    assert Solution().numberOfPairs([[3, 1], [1, 3], [1, 1]]) == 2
