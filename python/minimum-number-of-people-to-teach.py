# https://leetcode.com/problems/minimum-number-of-people-to-teach/


class Solution:
    @staticmethod
    def teachings_needed_for(
        language: int,
        languages: list[set[int]],
        friendships: list[list[int]],
    ) -> int:
        need_teaching = set()

        for u, v in friendships:
            if not (languages[u] & languages[v]):
                if language not in languages[u]:
                    need_teaching.add(u)
                if language not in languages[v]:
                    need_teaching.add(v)

        return len(need_teaching)

    def minimumTeachings(
        self,
        n: int,
        languages: list[list[int]],
        friendships: list[list[int]],
    ) -> int:
        language_sets: list[set[int]] = [set()] + [set(langs) for langs in languages]

        return min(
            Solution.teachings_needed_for(language, language_sets, friendships)
            for language in range(1, n + 1)
        )


if __name__ == "__main__":
    assert (
        Solution().minimumTeachings(
            11,
            [
                [3, 11, 5, 10, 1, 4, 9, 7, 2, 8, 6],
                [5, 10, 6, 4, 8, 7],
                [6, 11, 7, 9],
                [11, 10, 4],
                [6, 2, 8, 4, 3],
                [9, 2, 8, 4, 6, 1, 5, 7, 3, 10],
                [7, 5, 11, 1, 3, 4],
                [3, 4, 11, 10, 6, 2, 1, 7, 5, 8, 9],
                [8, 6, 10, 2, 3, 1, 11, 5],
                [5, 11, 6, 4, 2],
            ],
            [
                [7, 9],
                [3, 7],
                [3, 4],
                [2, 9],
                [1, 8],
                [5, 9],
                [8, 9],
                [6, 9],
                [3, 5],
                [4, 5],
                [4, 9],
                [3, 6],
                [1, 7],
                [1, 3],
                [2, 8],
                [2, 6],
                [5, 7],
                [4, 6],
                [5, 8],
                [5, 6],
                [2, 7],
                [4, 8],
                [3, 8],
                [6, 8],
                [2, 5],
                [1, 4],
                [1, 9],
                [1, 6],
                [6, 7],
            ],
        )
        == 0
    )

    assert (
        Solution().minimumTeachings(
            2,
            [[1], [2], [1, 2]],
            [[1, 2], [1, 3], [2, 3]],
        )
        == 1
    )

    assert (
        Solution().minimumTeachings(
            3,
            [[2], [1, 3], [1, 2], [3]],
            [[1, 4], [1, 2], [3, 4], [2, 3]],
        )
        == 2
    )
