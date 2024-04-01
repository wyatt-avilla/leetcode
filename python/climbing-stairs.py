# https://leetcode.com/problems/climbing-stairs/

from functools import lru_cache


class Solution:
    @lru_cache(maxsize=45)
    def climbStairs(self, current_step: int) -> int:
        if current_step == 0:
            return 1
        if current_step < 0:
            return 0

        return self.climbStairs(current_step - 1) + self.climbStairs(current_step - 2)


print(f"steps taken: {Solution().climbStairs(38)}")
