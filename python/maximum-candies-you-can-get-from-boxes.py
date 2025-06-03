# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/


class Solution:
    def maxCandies(
        self,
        status: list[int],
        candies: list[int],
        keys: list[list[int]],
        containedBoxes: list[list[int]],
        initialBoxes: list[int],
    ) -> int:
        candy = 0
        avail_keys: set[int] = set()
        encountered_but_locked = set()
        to_explore = set()
        for label in initialBoxes:
            if status[label] == 0:
                encountered_but_locked.add(label)
            else:
                to_explore.add(label)

        while len(to_explore) > 0:
            curr_box = to_explore.pop()
            candy += candies[curr_box]

            for label in keys[curr_box]:
                if label in encountered_but_locked:
                    encountered_but_locked.remove(label)
                    to_explore.add(label)
                avail_keys.add(label)
            keys[curr_box] = []

            for label in containedBoxes[curr_box]:
                if status[label] == 1:
                    to_explore.add(label)
                else:
                    if label in avail_keys:
                        to_explore.add(label)
                    else:
                        encountered_but_locked.add(label)
            containedBoxes[curr_box] = []

        return candy


if __name__ == "__main__":
    assert (
        Solution().maxCandies(
            [1, 1, 1],
            [100, 1, 100],
            [[], [0, 2], []],
            [[], [], []],
            [1],
        )
        == 1
    )

    assert (
        Solution().maxCandies(
            [1, 0, 1, 0],
            [7, 5, 4, 100],
            [[], [], [1], []],
            [[1, 2], [3], [], []],
            [0],
        )
        == 16
    )

    assert (
        Solution().maxCandies(
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [[1, 2, 3, 4, 5], [], [], [], [], []],
            [[1, 2, 3, 4, 5], [], [], [], [], []],
            [0],
        )
        == 6
    )
