# https://leetcode.com/problems/jump-game/

from __future__ import annotations


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        nums_len = len(nums)
        if all(nums) > 0 or (nums_len == 1):
            return True
        if nums[0] == 0 and nums_len > 1:
            return False

        reachable_from: list[list[int]] = [[] for _ in range(nums_len)]
        reachable_from[0]
        for i in range(nums_len - 1):
            if nums[i] > 0:
                for j in range(i + 1, i + 1 + nums[i]):
                    if j >= nums_len:
                        break
                    reachable_from[j].append(i)

        search_idxs: list[int] = reachable_from[nums_len - 1]
        seen_idxs: set[int] = set()
        while len(search_idxs) > 0:
            currently_searching = search_idxs.pop(0)
            if currently_searching in seen_idxs:
                continue
            if 0 in reachable_from[currently_searching]:
                return True
            search_idxs.extend(list(reachable_from[currently_searching]))
            seen_idxs.add(currently_searching)

        return False


cases = [
    ([1, 0, 1, 0], False),
    ([2, 3, 1, 1, 4], True),
    ([1, 1, 1, 1, 0], True),
    ([3, 2, 1, 0, 4], False),
    ([0, 1], False),
    ([0], True),
    ([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0], True),
    ([2, 0], True),
]

for case in cases:
    inp, exp = case
    res = Solution().canJump(inp)
    if exp != res:
        print(f"{inp} should yield {exp}")
