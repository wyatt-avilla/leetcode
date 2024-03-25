# https://leetcode.com/problems/find-the-difference-of-two-arrays

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        return [list(nums1_set - nums2_set), list(nums2_set - nums1_set)]


assert ({tuple(lst) for lst in Solution().findDifference([1, 2, 3], [2, 4, 6])}) == {
    (1, 3),
    (4, 6),
}

assert (
    {tuple(lst) for lst in Solution().findDifference([1, 2, 3, 3], [1, 1, 2, 2])}
) == {
    (3),
    (),
}
