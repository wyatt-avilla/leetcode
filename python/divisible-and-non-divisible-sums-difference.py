# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        multiples_in_n = n // m
        sum_to_n = n * (n + 1) // 2

        num2 = multiples_in_n * (multiples_in_n + 1) // 2 * m
        num1 = sum_to_n - num2

        return num1 - num2


if __name__ == "__main__":
    assert Solution().differenceOfSums(10, 3) == 19
    assert Solution().differenceOfSums(5, 6) == 15
    assert Solution().differenceOfSums(5, 1) == -15
