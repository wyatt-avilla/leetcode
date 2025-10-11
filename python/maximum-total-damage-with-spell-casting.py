# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        sorted_powers = [(-(10**9), 0), *sorted(Counter(power).items())]
        n = len(sorted_powers)
        dp = [0] * n

        mx = 0
        j = 1
        for i in range(1, n):
            while j < i and sorted_powers[j][0] < sorted_powers[i][0] - 2:
                mx = max(mx, dp[j])
                j += 1
            dp[i] = mx + sorted_powers[i][0] * sorted_powers[i][1]

        return max(dp)


if __name__ == "__main__":
    assert Solution().maximumTotalDamage([1, 1, 3, 4]) == 6
    assert Solution().maximumTotalDamage([7, 1, 6, 6]) == 13
