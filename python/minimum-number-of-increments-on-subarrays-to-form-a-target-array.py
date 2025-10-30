# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array


class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        n = len(target)
        ans = target[0]
        for i in range(1, n):
            ans += max(target[i] - target[i - 1], 0)
        return ans


if __name__ == "__main__":
    assert Solution().minNumberOperations([1, 2, 3, 2, 1]) == 3
    assert Solution().minNumberOperations([3, 1, 1, 2]) == 4
    assert Solution().minNumberOperations([3, 1, 5, 4, 2]) == 7
