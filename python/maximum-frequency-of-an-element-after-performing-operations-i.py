# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

from collections import Counter, defaultdict


class Solution:
    def maxFrequency(self, nums: list[int], k: int, num_operations: int) -> int:
        counts = Counter(nums)
        sweep: dict[int, int] = defaultdict(int)
        n = 100_000 + 2
        left = n
        right = 0

        for num in nums:
            x_0 = max(1, num - k)
            x_n = min(n - 1, num + k + 1)

            sweep[x_0] += 1
            sweep[x_n] -= 1

            left = min(left, x_0)
            right = max(right, x_n)

        count = ans = 0
        for i in range(left, right + 1):
            count += sweep[i]
            ans = max(ans, counts[i] + min(count - counts[i], num_operations))

        return ans


if __name__ == "__main__":
    assert Solution().maxFrequency([88, 53], 27, 2) == 2
    assert Solution().maxFrequency([1, 4, 5], 1, 2) == 2
    assert Solution().maxFrequency([5, 11, 20, 20], 5, 1) == 2
