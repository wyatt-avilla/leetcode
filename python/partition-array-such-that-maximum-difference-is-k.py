# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/


class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        low = nums[0]
        high = nums[0]
        count = 0
        for i in range(n):
            curr = nums[i]
            if curr > high:
                if abs(curr - low) <= k:
                    high = curr
                else:
                    count += 1
                    low = curr
                    high = curr

        return count + 1


if __name__ == "__main__":
    assert Solution().partitionArray([4, 0, 2, 1, 5], 2) == 2
    assert Solution().partitionArray([3, 6, 1, 2, 5], 2) == 2
    assert Solution().partitionArray([1, 2, 3], 1) == 2
    assert Solution().partitionArray([2, 2, 4, 5], 0) == 3
    assert Solution().partitionArray([1, 2, 3, 5, 7], 2) == 2
