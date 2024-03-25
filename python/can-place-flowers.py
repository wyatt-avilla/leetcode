# https://leetcode.com/problems/can-place-flowers/

from math import ceil
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed_len: int = len(flowerbed)
        valid_spaces: int = 0

        one_idxs: List[int] = [i for i, v in enumerate(flowerbed) if v == 1]
        for i in range(len(one_idxs) - 1):
            consecutive_zeros: int = one_idxs[i + 1] - one_idxs[i] - 1
            valid_spaces += ((consecutive_zeros // 2)) if consecutive_zeros > 0 else 0
            valid_spaces -= 1 if consecutive_zeros % 2 == 0 else 0

        if len(one_idxs) == 0:
            return n <= ceil(bed_len / 2)

        if 0 not in one_idxs:
            valid_spaces += one_idxs[0] // 2
        if bed_len - 1 not in one_idxs:
            valid_spaces += ((bed_len - 1) - one_idxs[-1]) // 2

        return n <= valid_spaces


assert Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1)
assert not Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2)
assert Solution().canPlaceFlowers([1, 0, 1, 0, 1], 0)
assert Solution().canPlaceFlowers([1, 0, 1, 0, 0, 0, 1], 1)
assert not Solution().canPlaceFlowers([1, 0, 1, 0, 0, 0, 1], 2)
assert not Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2)
assert not Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1, 0], 2)
assert Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1)
assert Solution().canPlaceFlowers([1, 0, 1, 0, 0], 1)
assert Solution().canPlaceFlowers([1, 0, 1, 0, 0], 0)
assert Solution().canPlaceFlowers([0], 1)
assert Solution().canPlaceFlowers([0, 0], 1)
assert Solution().canPlaceFlowers([0], 0)
assert Solution().canPlaceFlowers([0, 0, 0], 2)
assert not Solution().canPlaceFlowers([0, 0], 2)
