# https://leetcode.com/problems/top-k-frequent-elements/

from __future__ import annotations


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqdict: dict[int, int] = {
            x: nums.count(x) for x in range(min(nums), max(nums) + 1)
        }
        print(freqdict)
        freq_dict_descending = dict(
            sorted(freqdict.items(), key=lambda item: item[1], reverse=True),
        )
        print(freq_dict_descending)
        return list(freq_dict_descending)[:k]


assert set(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
assert set(Solution().topKFrequent([1], 1)) == {1}
assert set(Solution().topKFrequent([-1, -1], 1)) == {-1}
