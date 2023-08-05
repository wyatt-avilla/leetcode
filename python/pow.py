class Solution:
    def myPow(self, x: float, n: int) -> float:
        exp = 1
        for _ in range(abs(n)):
            exp *= x

        return exp if n > 0 else 1/abs(exp)





print(Solution().myPow(0.00001, 2147483647))
