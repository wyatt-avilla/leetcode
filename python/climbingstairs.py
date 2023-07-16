from functools import lru_cache


class Solution():

    @lru_cache(maxsize=45)
    def climbStairs(self, currentStep: int) -> int:
        if currentStep == 0:
            return 1
        if currentStep < 0:
            return 0

        return self.climbStairs(currentStep-1) + self.climbStairs(currentStep-2)


print(f"steps taken: {Solution().climbStairs(38)}")
