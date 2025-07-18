# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

from heapq import heapify, heappop, heappush


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 3
        max_heap = [-n for n in nums[:n]]
        min_heap = nums[2 * n :]

        heapify(max_heap)
        heapify(min_heap)

        max_heap_sum = sum(-n for n in max_heap)
        min_heap_sum = sum(min_heap)

        min_sum_at_idx = [max_heap_sum] + [0 for _ in range(n)]

        for i in range(n, 2 * n):
            max_heap_sum += nums[i]
            heappush(max_heap, -nums[i])
            max_heap_sum -= -heappop(max_heap)
            min_sum_at_idx[i - (n - 1)] = max_heap_sum

        ans = min_sum_at_idx[n] - min_heap_sum
        for i in range(n * 2 - 1, n - 1, -1):
            min_heap_sum += nums[i]
            heappush(min_heap, nums[i])
            min_heap_sum -= heappop(min_heap)
            ans = min(ans, min_sum_at_idx[i - n] - min_heap_sum)

        return ans


if __name__ == "__main__":
    assert Solution().minimumDifference([3, 1, 2]) == -1
    assert Solution().minimumDifference([7, 9, 5, 8, 1, 3]) == 1
    assert Solution().minimumDifference([1, 1, 0, 0, 2, 2]) == -4
    assert Solution().minimumDifference([0, 0, 2, 2, 1, 1]) == -4
