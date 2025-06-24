# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

import bisect


class Solution:
    def closest_within_k_distance(self, target: int, k: int, idxs: list[int]) -> bool:
        found_idx = bisect.bisect_left(idxs, target)
        left_adj = idxs[max(0, found_idx - 1)]
        right_adj = idxs[min(len(idxs) - 1, found_idx)]
        return min(abs(left_adj - target), abs(right_adj - target)) <= k

    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        key_idxs = [i for i, v in enumerate(nums) if v == key]
        return [
            i
            for i in range(len(nums))
            if self.closest_within_k_distance(i, k, key_idxs)
        ]


if __name__ == "__main__":
    assert Solution().findKDistantIndices([3, 4, 9, 1, 3, 9, 5], 9, 1) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]
    assert Solution().findKDistantIndices([2, 2, 2, 2, 2], 2, 2) == [0, 1, 2, 3, 4]
    assert Solution().findKDistantIndices([2, 1, 2, 3, 4, 2, 6, 7, 2, 9, 2], 2, 1) == [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    ]
